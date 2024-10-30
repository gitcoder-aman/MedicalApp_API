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
            "order_id":stockItem[2],
            "product_name":stockItem[3],
            "product_category":stockItem[4],
            "certified":stockItem[5],
            "product_price":stockItem[6],
            "product_stock":stockItem[7],
            "user_name":stockItem[8],
            "user_id":stockItem[9],
            
        }
        stockJson.append(tempStock)
    return json.dumps(stockJson)