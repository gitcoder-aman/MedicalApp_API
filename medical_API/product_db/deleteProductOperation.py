import sqlite3

def deleteProduct(productId):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Products WHERE product_id=?",(productId,))        
    conn.commit()
    conn.close()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Product Deleted successful. Rows affected:", cursor.rowcount)
        return 1
    else:
        print("No rows were Deleted. Check if the Product ID doesn't exists.")
        return 0