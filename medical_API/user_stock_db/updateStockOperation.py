import psycopg2
from db_config import get_connection

def updateStockAllFields(stockId, **keyword):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        field_map = {
            "user_id":          "user_id",
            "product_id":       "product_id",
            "product_name":     "product_name",
            "user_name":        "user_name",
            "certified":        "certified",
            "product_stock":    "product_stock",
            "product_price":    "product_price",
            "product_category": "product_category",
        }

        for key, value in keyword.items():
            if key in field_map:
                cursor.execute(
                    f"UPDATE Stocks SET {field_map[key]} = %s WHERE id = %s",
                    (value, stockId)
                )

        conn.commit()

        if cursor.rowcount > 0:
            print("Stocks Updated successfully. Rows affected:", cursor.rowcount)
            return 1
        else:
            print("No rows were updated. Check if the Stocks id doesn't exists.")
            return 0

    except psycopg2.OperationalError as e:
        print("OperationalError:", e)
        return 0
    finally:
        if conn:
            cursor.close()
            conn.close()