import psycopg2
from db_config import get_connection

def updateOrderAllFields(orderId, **keyword):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        field_map = {
            "isApproved":           "isApproved",
            "user_address":         "user_address",
            "user_pinCode":         "user_pinCode",
            "user_mobile":          "user_mobile",
            "user_email":           "user_email",
            "order_status":         "order_status",
            "order_cancel_status":  "order_cancel_status",
            "user_street":          "user_street",
            "user_city":            "user_city",
            "user_state":           "user_state",
            "shipped_date":         "shipped_date",
            "out_of_delivery_date": "out_of_delivery_date",
            "delivered_date":       "delivered_date",
        }

        for key, value in keyword.items():
            if key in field_map:
                cursor.execute(
                    f"UPDATE Orders SET {field_map[key]} = %s WHERE order_id = %s",
                    (value, orderId)
                )

        conn.commit()

        if cursor.rowcount > 0:
            print("Order Updated successfully. Rows affected:", cursor.rowcount)
            return 1
        else:
            print("No rows were updated. Check if the Order id doesn't exists.")
            return 0

    except psycopg2.OperationalError as e:
        print("OperationalError:", e)
        return 0
    finally:
        if conn:
            cursor.close()
            conn.close()