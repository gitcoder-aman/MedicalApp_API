import sqlite3

def deleteOrder(orderId):
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Orders WHERE order_id=?",(orderId,))        
    conn.commit()
    conn.close()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Order Deleted successful. Rows affected:", cursor.rowcount)
        return 1
    else:
        print("No rows were Deleted. Check if the Order ID doesn't exists.")
        return 0