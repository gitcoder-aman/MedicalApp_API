from db_config import get_connection

def createOrderTable():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            id                   SERIAL PRIMARY KEY,
            order_id             VARCHAR(255),
            user_id              VARCHAR(255),
            product_id           VARCHAR(255),
            product_name         VARCHAR(255),
            product_category     VARCHAR(255),
            product_image_id     TEXT,
            user_name            VARCHAR(255),
            isApproved           BOOLEAN,
            product_quantity     INT,
            product_price        FLOAT,
            subtotal_price       FLOAT,
            delivery_charge      FLOAT,
            tax_charge           FLOAT,
            total_price          FLOAT,
            order_date           DATE,
            user_address         VARCHAR(255),
            user_pinCode         VARCHAR(255),
            user_mobile          VARCHAR(255),
            user_email           VARCHAR(255),
            order_status         VARCHAR(255),
            order_cancel_status  VARCHAR(255),
            user_street          VARCHAR(255),
            user_city            VARCHAR(255),
            user_state           VARCHAR(255),
            discount_price       FLOAT,
            shipped_date         DATE,
            out_of_delivery_date DATE,
            delivered_date       DATE
        )
    """)

    # Fix existing table — Cloudinary URLs won't fit in VARCHAR(255)
    cursor.execute("""
        ALTER TABLE Orders
        ALTER COLUMN product_image_id TYPE TEXT
    """)

    conn.commit()
    cursor.close()
    conn.close()