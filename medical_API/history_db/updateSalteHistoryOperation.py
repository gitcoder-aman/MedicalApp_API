import psycopg2
from db_config import get_connection

def updateSellHistoryItemFields(sellId, **keyword):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        field_map = {
            "user_id":          "user_id",
            "product_id":       "product_id",
            "quantity":         "quantity",
            "remaining_stock":  "remaining_stock",
            "date_of_sell":     "date_of_sell",
            "total_amount":     "total_amount",
            "price":            "price",
            "product_name":     "product_name",
            "user_name":        "user_name",
            "product_category": "product_category",
        }

        for key, value in keyword.items():
            if key in field_map:
                cursor.execute(
                    f"UPDATE Sell_History SET {field_map[key]} = %s WHERE sell_id = %s",
                    (value, sellId)
                )

        conn.commit()

        if cursor.rowcount > 0:
            print("Sell History Updated successful. Rows affected:", cursor.rowcount)
            return 1
        else:
            print("No rows were updated. Check if the sell_id doesn't exists.")
            return 0

    except psycopg2.OperationalError as e:
        print("OperationalError:", e)
        return 0
    finally:
        if conn:
            cursor.close()
            conn.close()