import sqlite3
import uuid

def addOrderOperation(user_id,product_id,product_name,product_category,user_name,isApproved,product_quantity,product_price,subtotal_price,delivery_charge,tax_charge,totalPrice,orderDate):
    conn = sqlite3.connect("order.db")
    cursor = conn.cursor()

    order_id  = "O_"+str(uuid.uuid4())

    cursor.execute("""
                INSERT INTO Orders(
                  order_id,
                  user_id,
                  product_id,
                  product_name,
                  product_category,
                  user_name,
                  isApproved,
                  product_quantity,
                  product_price,
                  subtotal_price,
                  delivery_charge,
                  tax_charge,
                  total_price,
                  order_date
                   ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,(order_id,user_id,product_id,product_name,product_category,user_name,isApproved,product_quantity,product_price,subtotal_price,delivery_charge,tax_charge,totalPrice,orderDate))
         
    conn.commit()
    conn.close()

    return order_id