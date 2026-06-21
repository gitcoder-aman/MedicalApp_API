import json
from db_config import get_connection

def _row_to_history(h):
    return {
        "id":               h[0],
        "sell_id":          h[1],
        "product_id":       h[2],
        "quantity":         h[3],
        "remaining_stock":  h[4],
        "date_of_sell":     str(h[5]),
        "total_amount":     h[6],
        "price":            h[7],
        "product_name":     h[8],
        "product_category": h[9],
        "user_name":        h[10],
        "user_id":          h[11],
    }

def getAllSellHistoryItem():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sell_History")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_history(h) for h in items])

def getSpecificSellHistoryItem(sell_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sell_History WHERE sell_id = %s", (sell_id,))
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_history(h) for h in items])
