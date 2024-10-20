import sqlite3
import uuid

def addOrderOperation(user_id,product_id,product_name,product_category,product_image_id,user_name,isApproved,product_quantity,product_price,subtotal_price,delivery_charge,tax_charge,totalPrice,orderDate,user_address,user_pinCode,user_mobile,user_email):
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
                  product_image_id,
                  user_name,
                  isApproved,
                  product_quantity,
                  product_price,
                  subtotal_price,
                  delivery_charge,
                  tax_charge,
                  total_price,
                  order_date,
                  user_address,
                  user_pinCode,
                  user_mobile,
                  user_email
                   ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,(order_id,user_id,product_id,product_name,product_category,product_image_id,user_name,isApproved,product_quantity,product_price,subtotal_price,delivery_charge,tax_charge,totalPrice,orderDate,user_address,user_pinCode,user_mobile,user_email))
         
    conn.commit()
    conn.close()

    return order_id