import psycopg2
from db_config import get_connection

def updateProductAllFields(productId, **keyword):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        field_map = {
            "product_name":        "product_name",
            "product_category":    "product_category",
            "product_price":       "product_price",
            "product_expiry_date": "product_expiry_date",
            "product_rating":      "product_rating",
            "product_stock":       "product_stock",
            "product_description": "product_description",
            "product_power":       "product_power",
            "product_image_id":    "product_image_id",
        }

        for key, value in keyword.items():
            if key in field_map:
                cursor.execute(
                    f"UPDATE Products SET {field_map[key]} = %s WHERE product_id = %s",
                    (value, productId)
                )

        conn.commit()

        if cursor.rowcount > 0:
            print("Product Updated successful. Rows affected:", cursor.rowcount)
            return 1
        else:
            print("No rows were updated. Check if the Product id doesn't exists.")
            return 0

    except psycopg2.OperationalError as e:
        print("OperationalError:", e)
        return 0
    finally:
        if conn:
            cursor.close()
            conn.close()