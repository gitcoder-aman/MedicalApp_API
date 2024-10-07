import sqlite3

def createProductTable():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id VARCHAR(255),
        product_name VARCHAR(255),
        product_category VARCHAR(255),
        product_price INT,
        product_stock INT,
        product_expiry_date DATE,
        product_rating FLOAT,
        product_description VARCHAR(255),
        product_image VARCHAR(255),
        product_power VARCHAR(255)
        )
        '''
    )
    conn.commit()
    conn.close()