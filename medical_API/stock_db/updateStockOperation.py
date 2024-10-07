import sqlite3

def updateStockAllFields(stockId,**ketword):
    try:
     conn = sqlite3.connect("stock.db",timeout=10)
     cursor = conn.cursor()
     
     for key,value in ketword.items():
         if key == "user_id":
                cursor.execute("UPDATE Stocks SET user_id = ? WHERE id = ?",(value,stockId))
         elif key == "product_id":
                cursor.execute("UPDATE Stocks SET product_id = ? WHERE id = ?",(value,stockId))
         elif key == "product_name":
                cursor.execute("UPDATE Stocks SET product_name = ? WHERE id = ?",(value,stockId))
         elif key  == "user_name":
                               cursor.execute("UPDATE Stocks SET user_name = ? WHERE id = ?",(value,stockId))
         elif key  == "certified":
                               cursor.execute("UPDATE Stocks SET certified = ? WHERE id = ?",(value,stockId))
         elif key  == "stock":
                               cursor.execute("UPDATE Stocks SET stock = ? WHERE id = ?",(value,stockId))
         elif key  == "price":
                               cursor.execute("UPDATE Stocks SET price = ? WHERE id = ?",(value,stockId))
         elif key  == "product_category":
                               cursor.execute("UPDATE Stocks SET product_category = ? WHERE id = ?",(value,stockId))

     conn.commit()

     # Check if any rows were affected
     if cursor.rowcount > 0:
                print("Stocks Updated successfully. Rows affected:", cursor.rowcount)
                return 1
     else:
                print("No rows were updated. Check if the Stocks id doesn't exists.")
                return 0

    except sqlite3.OperationalError as e:
        print("OperationalError:", e)
    finally:
        # Close the connection
     conn.close()