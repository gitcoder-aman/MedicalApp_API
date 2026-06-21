from db_config import get_connection

def addStockOperation(product_id, product_name, category, certified, price, stock, user_name, user_id, order_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Stocks (
            product_id,
            product_name,
            product_category,
            certified,
            product_price,
            product_stock,
            user_name,
            user_id,
            order_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (product_id, product_name, category, certified, price, stock, user_name, user_id, order_id))

    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Add Stock successful. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were updated")
        return 0
