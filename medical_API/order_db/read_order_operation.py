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
            "product_image_id":orderItem[6],
            "user_name":orderItem[7],
            "isApproved":orderItem[8],
            "product_quantity":orderItem[9],
            "product_price":orderItem[10],
            "subtotal_price":orderItem[11],
            "delivery_charge":orderItem[12],
            "tax_charge":orderItem[13],
            "totalPrice":orderItem[14],
            "order_date":orderItem[15],
            "user_address":orderItem[16],
            "user_pinCode":orderItem[17],
            "user_mobile":orderItem[18],
            "user_email":orderItem[19]
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
            "product_image_id":orderItem[6],
            "user_name":orderItem[7],
            "isApproved":orderItem[8],
            "product_quantity":orderItem[9],
            "product_price":orderItem[10],
            "subtotal_price":orderItem[11],
            "delivery_charge":orderItem[12],
            "tax_charge":orderItem[13],
            "totalPrice":orderItem[14],
            "order_date":orderItem[15],
            "user_address":orderItem[16],
            "user_pinCode":orderItem[17],
            "user_mobile":orderItem[18],
            "user_email":orderItem[19]
        }
        
    orderJson.append(tempOrderSpecific)

    return json.dumps(orderJson)

def getAllOrderThroughUser(user_id):
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders WHERE user_id =?",(user_id,))
    ordersThroughId = cursor.fetchall()
    conn.close()

    orderThroughUserIdJson = []

    
    for orderItem in ordersThroughId:
        tempOrderThroughUserId = {
            "id" : orderItem[0],
            "order_id" : orderItem[1],
            "user_id":orderItem[2],
            "product_id":orderItem[3],
            "product_name":orderItem[4],
            "product_category":orderItem[5],
            "product_image_id":orderItem[6],
            "user_name":orderItem[7],
            "isApproved":orderItem[8],
            "product_quantity":orderItem[9],
            "product_price":orderItem[10],
            "subtotal_price":orderItem[11],
            "delivery_charge":orderItem[12],
            "tax_charge":orderItem[13],
            "totalPrice":orderItem[14],
            "order_date":orderItem[15],
            "user_address":orderItem[16],
            "user_pinCode":orderItem[17],
            "user_mobile":orderItem[18],
            "user_email":orderItem[19]
        }
        
        # Move the append statement inside the loop
        orderThroughUserIdJson.append(tempOrderThroughUserId)

    return json.dumps(orderThroughUserIdJson)
