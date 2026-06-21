import json
from db_config import get_connection

def _row_to_order(o):
    return {
        "id":                   o[0],
        "order_id":             o[1],
        "user_id":              o[2],
        "product_id":           o[3],
        "product_name":         o[4],
        "product_category":     o[5],
        "product_image_id":     o[6],
        "user_name":            o[7],
        "isApproved":           o[8],
        "product_quantity":     o[9],
        "product_price":        o[10],
        "subtotal_price":       o[11],
        "delivery_charge":      o[12],
        "tax_charge":           o[13],
        "totalPrice":           o[14],
        "order_date":           str(o[15]),
        "user_address":         o[16],
        "user_pinCode":         o[17],
        "user_mobile":          o[18],
        "user_email":           o[19],
        "order_status":         o[20],
        "order_cancel_status":  o[21],
        "user_street":          o[22],
        "user_city":            o[23],
        "user_state":           o[24],
        "discount_price":       o[25],
        "shipped_date":         str(o[26]) if o[26] else None,
        "out_of_delivery_date": str(o[27]) if o[27] else None,
        "delivered_date":       str(o[28]) if o[28] else None,
    }

def getAllOrderItem():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_order(o) for o in orders])

def getSpecificOrder(orderId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders WHERE order_id = %s", (orderId,))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_order(o) for o in orders])

def getAllOrderThroughUser(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders WHERE user_id = %s", (user_id,))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_order(o) for o in orders])
