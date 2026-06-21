from db_config import get_connection

def createStockTable():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stocks (
            id               SERIAL PRIMARY KEY,
            product_id       VARCHAR(255),
            order_id         VARCHAR(255),
            product_name     VARCHAR(255),
            product_category VARCHAR(255),
            certified        BOOLEAN,
            product_price    FLOAT,
            product_stock    INT,
            user_name        VARCHAR(255),
            user_id          VARCHAR(255)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
