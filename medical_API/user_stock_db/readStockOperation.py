import json
from db_config import get_connection

def getAllStockItem():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Stocks")
    stocks = cursor.fetchall()
    cursor.close()
    conn.close()

    stockJson = []
    for s in stocks:
        stockJson.append({
            "id":               s[0],
            "product_id":       s[1],
            "order_id":         s[2],
            "product_name":     s[3],
            "product_category": s[4],
            "certified":        s[5],
            "product_price":    s[6],
            "product_stock":    s[7],
            "user_name":        s[8],
            "user_id":          s[9],
        })
    return json.dumps(stockJson)