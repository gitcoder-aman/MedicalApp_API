import json
from db_config import get_connection

def _row_to_product(p):
    return {
        "id":                   p[0],
        "product_id":           p[1],
        "product_name":         p[2],
        "product_category":     p[3],
        "product_price":        p[4],
        "product_stock":        p[5],
        "product_expiry_date":  p[6],
        "product_rating":       p[7],
        "product_description":  p[8],
        "product_image_id":     p[9],
        "product_power":        p[10],
    }

def getAllProductItem():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_product(p) for p in products])

def getSpecificProductItem(productId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE product_id = %s", (productId,))
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_product(p) for p in products])
