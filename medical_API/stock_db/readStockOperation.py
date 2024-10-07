import sqlite3
import json

def getAllStockItem():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from Stocks")
    stocks = cursor.fetchall()
    conn.close()

    stockJson = []

    for stockItem in stocks:
        tempStock = {
            "id" : stockItem[0],
            "product_id" : stockItem[1],
            "product_name":stockItem[2],
            "product_category":stockItem[3],
            "certified":stockItem[4],
            "product_price":stockItem[5],
            "product_stock":stockItem[6],
            "user_name":stockItem[7],
            "user_id":stockItem[8]
        }
        stockJson.append(tempStock)
    return json.dumps(stockJson)