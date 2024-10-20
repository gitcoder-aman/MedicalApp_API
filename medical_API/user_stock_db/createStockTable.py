import sqlite3

def createStockTable():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

#yha badha dena hai stock
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Stocks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id VARCHAR(255),
        product_name VARCHAR(255),
        product_category VARCHAR(255),
        certified BOOLEAN,
        product_price INT,
        product_stock INT,
        user_name VARCHAR(255),
        user_id VARCHAR(255)
        )
        '''
    )
    conn.commit()
    conn.close()
