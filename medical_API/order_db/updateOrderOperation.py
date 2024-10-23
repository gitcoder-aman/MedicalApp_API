import sqlite3

def updateOrderAllFields(orderId,**ketword):
    try:
     conn = sqlite3.connect("order.db",timeout=10)
     cursor = conn.cursor()
     
     for key,value in ketword.items():
         if key == "isApproved":
                cursor.execute("UPDATE Orders SET isApproved = ? WHERE order_id = ?",(value,orderId))
         elif key == "user_address":
                cursor.execute("UPDATE Orders SET user_address = ? WHERE order_id = ?",(value,orderId))
         elif key == "user_pinCode":
                cursor.execute("UPDATE Orders SET user_pinCode = ? WHERE order_id = ?",(value,orderId))
         elif key  == "user_mobile":
                               cursor.execute("UPDATE Orders SET user_mobile = ? WHERE order_id = ?",(value,orderId))
         elif key  == "user_email":
                               cursor.execute("UPDATE Orders SET user_email = ? WHERE order_id = ?",(value,orderId))
         elif key  == "order_status":
                               cursor.execute("UPDATE Orders SET order_status = ? WHERE order_id = ?",(value,orderId))
         elif key  == "order_cancel_status":
                               cursor.execute("UPDATE Orders SET order_cancel_status = ? WHERE order_id = ?",(value,orderId))
         elif key  == "user_street":
                               cursor.execute("UPDATE Orders SET user_street = ? WHERE order_id = ?",(value,orderId))
         elif key  == "user_city":
                               cursor.execute("UPDATE Orders SET user_city = ? WHERE order_id = ?",(value,orderId))
         elif key  == "user_state":
                               cursor.execute("UPDATE Orders SET user_state = ? WHERE order_id = ?",(value,orderId))
                            

     conn.commit()

     # Check if any rows were affected
     if cursor.rowcount > 0:
                print("Order Updated successfully. Rows affected:", cursor.rowcount)
                return 1
     else:
                print("No rows were updated. Check if the Order id doesn't exists.")
                return 0

    except sqlite3.OperationalError as e:
        print("OperationalError:", e)
    finally:
        # Close the connection
     conn.close()