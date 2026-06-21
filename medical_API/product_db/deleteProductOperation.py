from db_config import get_connection

def deleteProduct(productId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Products WHERE product_id = %s", (productId,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Product Deleted successful. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were Deleted. Check if the Product ID doesn't exists.")
        return 0