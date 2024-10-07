import sqlite3

def updateSellHistoryItemFields(sellId,**ketword):
    try:
     conn = sqlite3.connect("sell_history.db",timeout=10)
     cursor = conn.cursor()
     
     for key,value in ketword.items():
         if key == "user_id":
                cursor.execute("UPDATE Sell_History SET user_id = ? WHERE sell_id = ?",(value,sellId))
         elif key == "product_id":
                cursor.execute("UPDATE Sell_History SET product_id = ? WHERE sell_id = ?",(value,sellId))
         elif key == "quantity":
                cursor.execute("UPDATE Sell_History SET quantity = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "remaining_stock":
                               cursor.execute("UPDATE Sell_History SET remaining_stock = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "date_of_sell":
                               cursor.execute("UPDATE Sell_History SET date_of_sell = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "total_amount":
                               cursor.execute("UPDATE Sell_History SET total_amount = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "price":
                               cursor.execute("UPDATE Sell_History SET price = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "product_name":
                               cursor.execute("UPDATE Sell_History SET product_name = ? WHERE sell_id = ?",(value,sellId))
         elif key  == "user_name":
                               cursor.execute("UPDATE Sell_History SET user_name = ? WHERE sell_id = ?",(value,sellId)) 
         elif key == "product_category"  :
                 cursor.execute("UPDATE Sell_History SET product_category = ? WHERE sell_id = ?",(value,sellId)) 

     conn.commit()

     # Check if any rows were affected
     if cursor.rowcount > 0:
                print("Product Updated successful. Rows affected:", cursor.rowcount)
                return 1
     else:
                print("No rows were updated. Check if the Product id doesn't exists.")
                return 0

    except sqlite3.OperationalError as e:
        print("OperationalError:", e)
    finally:
        # Close the connection
     conn.close()