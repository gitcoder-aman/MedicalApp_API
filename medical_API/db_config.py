import os
import json
import urllib.request
import urllib.parse


# ---------------------------------------------------------------------------
# Auto-detect connection mode:
#   PRODUCTION (Render / any cloud):  uses psycopg2 over port 5432
#   LOCAL DEV (ISP blocks port 5432): uses Neon HTTP API over port 443
#
# Set USE_PSYCOPG2=true in your Render env vars to force psycopg2.
# Locally it auto-detects by attempting a quick socket test.
# ---------------------------------------------------------------------------

def _port_reachable(host, port=5432, timeout=3):
    """Quick check: can we reach host:port?"""
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0


def _use_psycopg2():
    """Return True if psycopg2 direct connection should be used."""
    # Explicit override via env var (set USE_PSYCOPG2=true on Render)
    override = os.getenv("USE_PSYCOPG2", "").lower()
    if override == "true":
        return True
    if override == "false":
        return False
    # Auto-detect: check if port 5432 is reachable
    dsn = os.getenv("DATABASE_URL", "")
    try:
        host = urllib.parse.urlparse(dsn).hostname or ""
        return _port_reachable(host, 5432, timeout=3)
    except Exception:
        return False


# ============================================================
#  PSYCOPG2 PATH  (production: Render, Railway, VPS, etc.)
# ============================================================

def _get_psycopg2_connection(dsn):
    import psycopg2
    return psycopg2.connect(dsn)


# ============================================================
#  NEON HTTP API PATH  (local dev: ISP blocks port 5432)
# ============================================================

class NeonHTTPCursor:
    """Minimal psycopg2-compatible cursor backed by Neon's HTTPS SQL API."""

    def __init__(self, conn):
        self._conn = conn
        self.rowcount = -1
        self._rows = []
        self._pos = 0

    def execute(self, query, params=None):
        if params:
            query = self._interpolate(query, params)
        payload = json.dumps({"query": query, "params": []}).encode()
        headers = {
            "Content-Type": "application/json",
            "Neon-Connection-String": self._conn._dsn,
        }
        url = f"https://{self._conn._host}/sql"
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        self._rows = [list(r.values()) for r in data.get("rows", [])]
        self._pos = 0
        self.rowcount = data.get("rowCount", 0)
        if self.rowcount == 0 and self._rows:
            self.rowcount = len(self._rows)

    def executemany(self, query, seq_of_params):
        for params in seq_of_params:
            self.execute(query, params)

    def fetchone(self):
        if self._pos < len(self._rows):
            row = self._rows[self._pos]
            self._pos += 1
            return row
        return None

    def fetchall(self):
        rows = self._rows[self._pos:]
        self._pos = len(self._rows)
        return rows

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @staticmethod
    def _interpolate(query, params):
        from datetime import date, datetime
        result = []
        param_iter = iter(params)
        i = 0
        while i < len(query):
            if query[i] == '%' and i + 1 < len(query) and query[i + 1] == 's':
                val = next(param_iter)
                result.append(NeonHTTPCursor._to_sql(val))
                i += 2
            else:
                result.append(query[i])
                i += 1
        return ''.join(result)

    @staticmethod
    def _to_sql(val):
        from datetime import date, datetime
        if val is None:
            return 'NULL'
        if isinstance(val, bool):
            return 'TRUE' if val else 'FALSE'
        if isinstance(val, (int, float)):
            return str(val)
        if isinstance(val, (date, datetime)):
            return f"'{val}'"
        return "'" + str(val).replace("'", "''") + "'"


class NeonHTTPConnection:
    """Minimal psycopg2-compatible connection backed by Neon's HTTPS SQL API."""

    def __init__(self, dsn):
        self._dsn = dsn
        parsed = urllib.parse.urlparse(dsn)
        self._host = parsed.hostname

    def cursor(self):
        return NeonHTTPCursor(self)

    def commit(self):
        pass   # Neon HTTP API auto-commits each statement

    def rollback(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# ============================================================
#  PUBLIC API
# ============================================================

def get_connection():
    """
    Returns a DB connection.
    - On Render / cloud (port 5432 open): uses psycopg2 (fast, full-featured).
    - On local dev (ISP blocks 5432):     uses Neon HTTP API over port 443.

    Environment variables:
      DATABASE_URL   - Neon PostgreSQL connection string (required)
      USE_PSYCOPG2   - 'true' to force psycopg2, 'false' to force HTTP API
                       (leave unset for auto-detect)
    """
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        raise EnvironmentError(
            "DATABASE_URL environment variable is not set.\n"
            "Copy .env.example to .env and fill in your Neon connection string."
        )

    if _use_psycopg2():
        return _get_psycopg2_connection(dsn)
    else:
        return NeonHTTPConnection(dsn)