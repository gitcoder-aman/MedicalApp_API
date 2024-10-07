import sqlite3
import uuid

def addSellHistoryOperation(user_id,product_id,product_name,user_name,quantity,remaining_stock,price,product_category,date_of_sell,total_amount):
    conn = sqlite3.connect("sell_history.db")
    cursor = conn.cursor()

    sell_id  = "H_"+str(uuid.uuid4())

    cursor.execute("""
                INSERT INTO Sell_History(
                  sell_id,
                  product_id,
                  quantity,
                  remaining_stock,
                  date_of_sell,
                  total_amount,
                  price,
                  product_name,
                  product_category,
                  user_name,
                  user_id) VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """,(sell_id,product_id,quantity,remaining_stock,date_of_sell,total_amount,price,product_name,product_category,user_name,user_id))
         
    conn.commit()
    conn.close()

    return sell_id
