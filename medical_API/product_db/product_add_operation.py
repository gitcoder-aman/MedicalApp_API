import uuid
from db_config import get_connection

def addProductOperation(name, category, price, stock, expiry_date, rating, description, image, power):
    conn = get_connection()
    cursor = conn.cursor()

    product_id = "P_" + str(uuid.uuid4())

    cursor.execute("""
        INSERT INTO Products (
            product_id,
            product_name,
            product_category,
            product_price,
            product_stock,
            product_expiry_date,
            product_rating,
            product_description,
            product_image_id,
            product_power
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (product_id, name, category, price, stock, expiry_date, rating, description, image, power))

    conn.commit()
    cursor.close()
    conn.close()

    return product_id
