import sqlite3
import json

def getAllProductItem():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from Products")
    products = cursor.fetchall()
    conn.close()

    productJson = []

    for productItem in products:
        tempProduct = {
            "id" : productItem[0],
            "product_id" : productItem[1],
            "product_name":productItem[2],
            "product_category":productItem[3],
            "product_price":productItem[4],
            "product_stock":productItem[5],
            "product_expiry_date":productItem[6],
            "product_rating":productItem[7],
            "product_description":productItem[8],
            "product_image_id":productItem[9],
            "product_power":productItem[10]
        }
        productJson.append(tempProduct)
    return json.dumps(productJson)

def getSpecificProductItem(productId):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE product_id =?",(productId,))
    products = cursor.fetchall()
    conn.close()

    productJson = []

    for productItem in products:
        tempProduct = {
            "id" : productItem[0],
            "product_id" : productItem[1],
            "product_name":productItem[2],
            "product_category":productItem[3],
            "product_price":productItem[4],
            "product_stock":productItem[5],
            "product_expiry_date":productItem[6],
            "product_rating":productItem[7],
            "product_description":productItem[8],
            "product_image_id":productItem[9],
            "product_power":productItem[10]
        }
        productJson.append(tempProduct)
    return json.dumps(productJson)

