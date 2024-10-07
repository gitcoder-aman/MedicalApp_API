import sqlite3

def createOrderTable():
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id VARCHAR(255),
        user_id VARCHAR(255),
        product_id VARCHAR(255),
        product_name VARCHAR(255),
        product_category VARCHAR(255),
        user_name VARCHAR(255),
        isApproved BOOLEAN,
        product_quantity INT,
        product_price FLOAT,
        subtotal_price FLOAT,
        delivery_charge FLOAT,
        tax_charge FLOAT,
        total_price FLOAT,
        order_date DATE
        )
        '''
    )
    conn.commit()
    conn.close()