import sqlite3
import json

def getAllOrderItem():
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from Orders")
    orders = cursor.fetchall()
    conn.close()

    ordersJson = []

    for orderItem in orders:
        tempOrder = {
            "id" : orderItem[0],
            "order_id" : orderItem[1],
            "user_id":orderItem[2],
            "product_id":orderItem[3],
            "product_name":orderItem[4],
            "product_category":orderItem[5],
            "user_name":orderItem[6],
            "isApproved":orderItem[7],
            "product_quantity":orderItem[8],
            "product_price":orderItem[9],
            "subtotal_price":orderItem[10],
            "delivery_charge":orderItem[11],
            "tax_charge":orderItem[12],
            "totalPrice":orderItem[13],
            "order_date":orderItem[14],
        }
        ordersJson.append(tempOrder)
    return json.dumps(ordersJson)


def getSpecificOrder(orderId):
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders WHERE order_id =?",(orderId,))
    orders = cursor.fetchall()
    conn.close()

    orderJson = []

    for orderItem in orders:
          tempOrderSpecific = {
            "id" : orderItem[0],
            "order_id" : orderItem[1],
            "user_id":orderItem[2],
            "product_id":orderItem[3],
            "product_name":orderItem[4],
            "product_category":orderItem[5],
            "user_name":orderItem[6],
            "isApproved":orderItem[7],
            "product_quantity":orderItem[8],
            "product_price":orderItem[9],
            "subtotal_price":orderItem[10],
            "delivery_charge":orderItem[11],
            "tax_charge":orderItem[12],
            "totalPrice":orderItem[13],
            "order_date":orderItem[14],
        }
        
    orderJson.append(tempOrderSpecific)

    return json.dumps(orderJson)