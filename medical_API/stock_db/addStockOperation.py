import sqlite3

def addStockOperation(product_id,product_name,category,certified,price,stock,user_name,user_id):
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

    cursor.execute("""
                INSERT INTO Stocks(
                  product_id,
                  product_name,
                  product_category,
                  certified,
                  product_price,
                  product_stock,
                  user_name,
                  user_id) VALUES (?,?,?,?,?,?,?,?)
            """,(product_id,product_name,category,certified,price,stock,user_name,user_id))
         
    conn.commit()
    conn.close()


      # Check if any rows were affected
    if cursor.rowcount > 0:
                print("Update successful. Rows affected:", cursor.rowcount)
                return 1
    else:
                print("No rows were updated. Check if the userId exists.")
                return 0

