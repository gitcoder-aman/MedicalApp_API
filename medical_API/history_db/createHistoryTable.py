import sqlite3

def createHistoryTable():
    #database create
    conn = sqlite3.connect("sell_history.db")
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Sell_History(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sell_id VARCHAR(255),
                   product_id VARCHAR(255),
                   quantity INT,
                   remaining_stock INT,
                   date_of_sell DATE,
                   total_amount FLOAT,
                   price FLOAT,
                   product_name VARCHAR(255),
                   product_category VARCHAR(255),
                   user_name VARCHAR(255),
                   user_id VARCHAR(255))
    ''')
    conn.commit()
    conn.close()