from db_config import get_connection

def createProductTable():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id                  SERIAL PRIMARY KEY,
            product_id          VARCHAR(255),
            product_name        VARCHAR(255),
            product_category    VARCHAR(255),
            product_price       FLOAT,
            product_stock       INT,
            product_expiry_date VARCHAR(255),
            product_rating      FLOAT,
            product_description VARCHAR(255),
            product_image_id    VARCHAR(255),
            product_power       VARCHAR(255)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()