import sqlite3

def updateProductAllFields(productId,**ketword):
    try:
     conn = sqlite3.connect("product.db",timeout=10)
     cursor = conn.cursor()
     
     for key,value in ketword.items():
         if key == "product_name":
                cursor.execute("UPDATE Products SET product_name = ? WHERE product_id = ?",(value,productId))
         elif key == "product_category":
                cursor.execute("UPDATE Products SET product_category = ? WHERE product_id = ?",(value,productId))
         elif key == "product_price":
                cursor.execute("UPDATE Products SET product_price = ? WHERE product_id = ?",(value,productId))
         elif key  == "product_expiry_date":
                               cursor.execute("UPDATE Products SET product_expiry_date = ? WHERE product_id = ?",(value,productId))
         elif key  == "product_rating":
                               cursor.execute("UPDATE Products SET product_rating = ? WHERE product_id = ?",(value,productId))
         elif key  == "product_stock":
                               cursor.execute("UPDATE Products SET product_stock = ? WHERE product_id = ?",(value,productId))
         elif key  == "product_description":
                               cursor.execute("UPDATE Products SET product_description = ? WHERE product_id = ?",(value,productId))
         elif key  == "product_power":
                               cursor.execute("UPDATE Products SET product_power = ? WHERE product_id = ?",(value,productId))   

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