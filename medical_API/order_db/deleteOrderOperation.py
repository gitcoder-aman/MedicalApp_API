from db_config import get_connection

def deleteOrder(orderId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Orders WHERE order_id = %s", (orderId,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Order Deleted successful. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were Deleted. Check if the Order ID doesn't exists.")
        return 0