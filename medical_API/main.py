from flask import Flask,jsonify,request,Response
from werkzeug.utils import secure_filename
from uploadImg.db import db_init,db
from uploadImg.models import Img


from user_db.createTableOpration import createUserTables
from user_db.addOperation import createUser
from user_db.updateOperation import updateUserName,updateUserAllFields
from user_db.readOperation import getAllUsers,getSpecificUser
from user_db.deleteOperation import deleteUserOperation
from user_db.auth import user_auth

from product_db.createProductTable import createProductTable
from product_db.product_add_operation import addProductOperation
from product_db.readProductOperation import getAllProductItem,getSpecificProductItem
from product_db.updateProductOperation import updateProductAllFields
from product_db.deleteProductOperation import deleteProduct

from order_db.createOrderDb import createOrderTable
from order_db.read_order_operation import getAllOrderItem,getSpecificOrder,getAllOrderThroughUser
from order_db.order_add_operation import addOrderOperation
from order_db.deleteOrderOperation import deleteOrder
from order_db.updateOrderOperation import updateOrderAllFields

from user_stock_db.createStockTable import createStockTable
from user_stock_db.readStockOperation import getAllStockItem
from user_stock_db.addStockOperation import addStockOperation
from user_stock_db.updateStockOperation import updateStockAllFields
from user_stock_db.deleteStockOperation import deleteStock

from history_db.createHistoryTable  import createHistoryTable
from history_db.addHistoryOperation import addSellHistoryOperation
from history_db.readHistoryOperation import getAllSellHistoryItem,getSpecificSellHistoryItem
from history_db.deleteSellHistoryOperation import deleteSellHistroyItem
from history_db.updateSalteHistoryOperation import updateSellHistoryItemFields

app = Flask(__name__)   # app is just a variable (create a instance)

# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

# @app.route('/upload', methods=['POST'])
# def upload():
#     pic = request.files['pic']
#     if not pic:
#         return 'No pic uploaded!', 400

#     filename = secure_filename(pic.filename)
#     mimetype = pic.mimetype
#     if not filename or not mimetype:
#         return 'Bad upload!', 400

#     img = Img(img=pic.read(), name=filename, mimetype=mimetype)
#     db.session.add(img)
#     db.session.commit()

#     return 'Img Uploaded!', 200

@app.route('/getImg/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

@app.route('/',methods=['GET'])
def home():
    return "Hello World!"

#USER API
@app.route('/signup',methods=['POST'])
def signup():

    try:
        name = request.form['userName']  #field name
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phoneNumber']
        address = request.form['address']
        pinCode = request.form['pinCode']

        # pic = request.files['pic']
        # if not pic:
        #    userImageId = -1
        # else:
        #  filename = secure_filename(pic.filename)
        #  mimetype = pic.mimetype
        #  if not filename or not mimetype:
        #      return 'Bad upload!', 400

        #  img = Img(img=pic.read(), name=filename, mimetype=mimetype)
        #  db.session.add(img)
        #  db.session.flush()  # Ensure that the ID is assigned before committing
        #  userImageId = img.id
        #  db.session.commit()


        if(validate_user(name,password,email)):
                data = createUser(
                name=name,
                password=password,
                phone_number=phone,
                email=email,
                pinCode=pinCode,
                address=address,
                userImageId = -1
           )
        else:
             return jsonify({"status": 400, "message": "Mandatory field empty"})
                 
        if data:
            return jsonify({"status" : 200,"message" : data})
        else:
            return jsonify({"status" : 400,"message":data})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    

def validate_user(name, password, email):
    if not name or not password or not email:
        return 0
    else:
         return 1
    
@app.route("/getSpecificUser",methods=['POST'])
def getSpecificUserMain():
     try:
          userId = request.form['userId']
          getUserInfo = getSpecificUser(userId = userId)
          return getUserInfo
     
     except Exception as e:
        return jsonify({"status":400,"message":str(e)})


@app.route('/getAllUsers',methods=['GET'])
def getAllUser():
    return getAllUsers()

@app.route('/login',methods=['POST'])
def login():
        
        try:
            email = request.form['email']
            password = request.form['password']

            loginData = user_auth(
            email=email,
            password=password,
            ) 

            if loginData:
                return jsonify({"status" : 200,"message" : loginData[1]})
            else:
                return jsonify({"status" : 200,"message":loginData})
        except Exception as e:
             return jsonify({"status":400,"message":str(e)})

@app.route('/updateUserName',methods=['PATCH'])
def updateUserNameMain():
     try:
          newName = request.form['updateName']
          userId = request.form['userId']

          isUpdate = updateUserName(userId = userId,name = newName)
               
          if(isUpdate):  
                return jsonify({"status":200,"message":"User Name Updated Successfully"})
          else:
                return jsonify({"status":400,"message":"User Id not found!"})
     
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})
     
@app.route('/updateUser', methods=['PATCH'])
def updateUserData():
    try:
        userId = request.form['userId']

        allFields = request.form.items()
        updateUser = {}
        user_image_id = None  # Initialize user image ID


        for key, value in allFields:
            if key != 'userId':
                updateUser[key] = value

        # Check for the 'pic' file in the request
        pic = request.files.get('pic')  # Use .get() to avoid KeyError

        if pic and pic.filename:  # Check if a file is provided
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            if not filename or not mimetype:
                return jsonify({'status': 400, 'message': 'Bad upload!'}), 400
            
            new_img = Img(img=pic.read(), name=filename, mimetype=mimetype)
            db.session.add(new_img)
            db.session.flush()  # Get the new image ID
            user_image_id = new_img.id

            # Link this new image to the user
            updateUser['user_image_id'] = user_image_id  # Associate the new image ID
            
# Only update if there are fields to update
        if updateUser:
            isUpdated = updateUserAllFields(userId=userId, **updateUser)

            if isUpdated:  
                db.session.commit()  # Commit the session only after successful update
                return jsonify({"status": 200, "message": "Data updated"})
            else:
                return jsonify({"status": 400, "message": "Data not updated"})
        else:
            return jsonify({"status": 400, "message": "No fields to update"})

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"status": 400, "message": str(e)})

@app.route('/deleteUser',methods=['DELETE'])
def deleteUser():
     try:
          userId = request.args.get('userId')
          isDeleted = deleteUserOperation(userId=userId)

          if(isDeleted):  
                return jsonify({"status":200,"message":"User Data Deleted Successfully"})
          else:
                return jsonify({"status":400,"message":"User Id not found!"})
     
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})

#Product API
@app.route('/addProduct',methods=['POST'])
def addProduct():
    try:
        name = request.form['product_name']
        category = request.form['product_category']
        price = request.form['product_price']
        stock = request.form['product_stock']
        expiry_date = request.form['product_expiry_date']
        rating = request.form['product_rating']
        description = request.form['product_description']
        power = request.form['product_power']       

    
        pic = request.files['pic']
        if not pic:
           return 'No pic uploaded!', 400

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        if not filename or not mimetype:
             return 'Bad upload!', 400

        img = Img(img=pic.read(), name=filename, mimetype=mimetype)
        db.session.add(img)
        db.session.commit()
    
        if(validate_product(name,category,price,stock,expiry_date,rating,description,power)):
               product_id = addProductOperation(
                name=name,
                category=category,
                price=price,
                stock=stock,
                expiry_date=expiry_date,
                rating=rating,
                description=description,
                image=img.id,
                power=power
            )
        else:
             return jsonify({"status": 400, "message": "Mandatory field empty"})
                 
        if product_id:
              return jsonify({"status" : 200,"message" : product_id})
        else:
            return jsonify({"status" : 400,"message":product_id})
    except Exception as e:
           return jsonify({"status":400,"message":str(e)})      

def validate_product(name,category,price,stock,expiry_date,rating,description,power):
    if not name or not category or not price or not stock or not expiry_date or not rating or not description or not power:
        return 0
    else:
         return 1
    
@app.route('/getAllProduct',methods=['GET'])
def getAllProduct():
    return getAllProductItem()

@app.route('/getSpecificProduct',methods=['POST'])
def getSpecificProduct():
    try:
          productId = request.form['productId']
          getProductInfo = getSpecificProductItem(productId = productId)
          return getProductInfo
     
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})

@app.route('/updateProduct',methods=['PATCH'])
def updateProductOperation():
     try:
          productId = request.form['productId']

          allFields = request.form.items()
          updateProduct = {}
          product_image_id = None

          for key,value in allFields:
               if key != 'productId':
                    updateProduct[key] = value

        # Check for the 'pic' file in the request   
          pic = request.files.get('pic')
          if pic and pic.filename:  # Check if a file is provided
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            if not filename or not mimetype:
                return jsonify({'status': 400, 'message': 'Bad upload!'}), 400
            
            new_img = Img(img=pic.read(), name=filename, mimetype=mimetype)
            db.session.add(new_img)
            db.session.flush()  # Get the new image ID
            product_image_id = new_img.id
            # Link this new image to the user
            updateProduct['product_image_id'] = product_image_id

          if updateProduct:
             isUpdated = updateProductAllFields(productId,**updateProduct)

             if isUpdated:
                  db.session.commit()
                  return jsonify({"status": 200, "message": "Data updated"})
             else:
                return jsonify({"status": 400, "message": "Data not updated"})

          else:
            return jsonify({"status": 400, "message": "No fields to update"})

     except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"status": 400, "message": str(e)})     
     
@app.route('/deleteProduct',methods=['DELETE'])
def deleteProductOperation():
     try:
          productId = request.args.get('productId')
          isDeleted = deleteProduct(productId=productId)

          if(isDeleted):  
                return jsonify({"status":200,"message":"Product Deleted Successfully"})
          else:
                return jsonify({"status":400,"message":"Product Id not found!"})
     
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})

#Order API
@app.route('/order',methods=['POST'])
def order():

    try:
        user_id = request.form['user_id']  #field name
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        product_category = request.form['product_category']
        product_image_id = request.form['product_image_id']
        user_name = request.form['user_name']
        isApproved = request.form['isApproved']
        quantity = request.form['product_quantity']
        price = request.form['product_price']
        subtotalPrice = request.form['subtotal_price']
        deliveryCharge = request.form['delivery_charge']
        taxCharge = request.form['tax_charge']
        totalPrice = request.form['total_price']
        orderDate = request.form['order_date']
        user_address = request.form['user_address']
        user_pinCode = request.form['user_pincode']
        user_mobile = request.form['user_mobile']
        user_email = request.form['user_email']
        order_status = request.form['order_status']
        order_cancel_status = request.form['order_cancel_status']
        user_street = request.form['user_street']
        user_city = request.form['user_city']
        user_state = request.form['user_state']
        discountPrice = request.form['discount_price']
        shipped_date = request.form['shipped_date']
        out_of_delivery_date = request.form['out_of_delivery_date']
        delivered_date = request.form['delivered_date']

        if(validate_order_data(user_id,product_id,product_name,product_category,product_image_id,user_name,
                               isApproved,quantity,price,subtotalPrice,totalPrice,orderDate,user_address,user_pinCode,user_mobile,user_email,order_status,
                               order_cancel_status,user_street,user_state,user_city,discountPrice)):
                orderId = addOrderOperation(
                user_id=user_id,
                product_id=product_id,
                product_name=product_name,
                user_name=user_name,
                isApproved=isApproved,
                product_quantity=quantity,
                product_price=price,
                totalPrice=totalPrice,
                orderDate=orderDate,
                product_category=product_category,
                product_image_id = product_image_id,
                subtotal_price=subtotalPrice,
                tax_charge=taxCharge,
                delivery_charge=deliveryCharge,
                user_email=user_email,
                user_address=user_address,
                user_mobile=user_mobile,
                user_pinCode=user_pinCode,
                order_status=order_status,
                order_cancel_status=order_cancel_status,
                user_street=user_street,
                user_city=user_city,
                user_state=user_state,
                discountPrice=discountPrice,
                shipped_date=shipped_date,
                out_of_delivery_date=out_of_delivery_date,
                delivered_date=delivered_date
           )
        else:
             return jsonify({"status": 400, "message": "Mandatory field empty"})
                 
        if orderId:
            return jsonify({"status" : 200,"message" : orderId})
        else:
            return jsonify({"status" : 400,"message":orderId})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
def validate_order_data(user_id,product_id,product_name,product_category,product_image_id,user_name,isApproved,quantity,price,subtotalPrice,totalPrice,orderDate,user_address,user_pinCode,user_mobile,
                        user_email,order_status,order_cancel_status,user_street,user_city,user_state,discountPrice):
    if not user_id or not product_id or not product_name or not user_name or not isApproved or not quantity or not price or not totalPrice or not orderDate or not product_category or not product_image_id or not subtotalPrice or not user_address or not user_pinCode or not user_mobile or not user_email or not order_status or not order_cancel_status or not user_state or not user_street or not discountPrice or not user_city:
        return 0
    else:
         return 1

@app.route('/getAllOrders',methods=['GET'])
def getAllOrder():
     return getAllOrderItem()

@app.route('/updateOrder',methods=['PATCH'])
def updateOrderOperation():
     try:
          orderId = request.form['orderId']

          allFields = request.form.items()
          updateOrder = {}

          for key,value in allFields:
               if key != 'orderId':
                    updateOrder[key] = value

          isUpdated = updateOrderAllFields(orderId,**updateOrder)

          if(isUpdated):  
                 return jsonify({"status":200,"message":"data updated Successfull"})
          else:
                return jsonify({"status":400,"message":"Order Id not found!"})
                    
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})
     

@app.route('/getSpecificOrder',methods=['POST'])
def getSpecificOrderMain():
     try:
          orderId = request.form['order_id']
          getOrderInfo = getSpecificOrder(orderId = orderId)
          return getOrderInfo
     
     except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
@app.route('/getAllOrderThroughUser',methods=['POST'])
def getAllOrderThroughUserMain():
     try:
          userId = request.form['user_id']
          getAllOrderThroughUserList = getAllOrderThroughUser(user_id = userId)
          return getAllOrderThroughUserList
     
     except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
@app.route('/deleteOrder',methods=['DELETE'])
def deleteOrderOperation():
    try:
          orderId = request.form['order_id']
          isDeleted = deleteOrder(orderId=orderId)

          if(isDeleted):  
                return jsonify({"status":200,"message":"Order Deleted Successfully"})
          else:
                return jsonify({"status":400,"message":"Order Id not found!"})
     
    except Exception as e:
          return jsonify({"status":400,"message":str(e)})

#Stock API

@app.route('/stock',methods=['POST'])
def stock():

    try:
        user_id = request.form['user_id']  #field name
        product_id = request.form['product_id']
        order_id = request.form['order_id']
        product_name = request.form['product_name']
        user_name = request.form['user_name']
        certified = request.form['certified']
        stock = request.form['stock']
        price = request.form['price']
        category = request.form['product_category']

        if(validate_stock_data(user_id,product_id,product_name,user_name,certified,stock,price,category,order_id)):
            stockId = addStockOperation(
                user_id=user_id,
                user_name=user_name,
                product_id=product_id,
                category=category,
                product_name=product_name,
                certified=certified,
                price=price,
                stock=stock,
                order_id=order_id
           )
        else:
             return jsonify({"status": "Invalid User", "message": "Mandatory field empty"})
                 
        if stockId:
            return jsonify({"status" : 200,"message" : "Stock Product added."})
        else:
            return jsonify({"status" : 400 ,"message":"Something went wrong."})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
def validate_stock_data(user_id,product_id,product_name,user_name,certified,stock,price,category,order_id):
    if not user_id or not product_id or not product_name or not user_name or not certified or not stock or not price or not category or not order_id:
        return 0
    else:
         return 1

@app.route('/getAllStock',methods=['GET'])
def getAllStock():
     return getAllStockItem()

@app.route('/stockUpdate',methods=['PATCH'])
def stockUpdateOperation():
    try:
        stockId = request.form['stock_id']

        allFields = request.form.items()
        updateStock = {}

        for key,value in allFields:
                    if key != 'stock_id':
                            updateStock[key] = value

        isUpdated = updateStockAllFields(stockId,**updateStock)
        if(isUpdated):  
                    return jsonify({"status":200,"message":"Stock updated Successfull"})
        else:
                    return jsonify({"status":400,"message":"Stock Id not found!"})
                          
    except Exception as e:
              return jsonify({"status":400,"message":str(e)})

@app.route('/deleteStock',methods=['DELETE'])
def deleteStockOperation():
    try:
          stockId = request.form['stock_id']
          isDeleted = deleteStock(stockId=stockId)

          if(isDeleted):  
                return jsonify({"status":200,"message":"Stock Deleted Successfully"})
          else:
                return jsonify({"status":400,"message":"Stock Id not found!"})
     
    except Exception as e:
          return jsonify({"status":400,"message":str(e)})


#sell history API
@app.route('/sell_history',methods=['POST'])
def sell_History():
    try:
        user_id = request.form['user_id']  #field name
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        remaining_stock = request.form['remaining_stock']
        date_of_sell = request.form['date_of_sell']
        total_amount = request.form['total_amount']
        price = request.form['price']
        product_name = request.form['product_name']
        user_name = request.form['user_name']
        product_category = request.form['product_category']

        if(validate_history_data(user_id,product_id,product_name,user_name,quantity,remaining_stock,price,product_category,date_of_sell,total_amount)):
            stockId = addSellHistoryOperation(
                user_id=user_id,
                user_name=user_name,
                product_id=product_id,
                product_category=product_category,
                product_name=product_name,
                price=price,
                remaining_stock=remaining_stock,
                date_of_sell=date_of_sell,
                total_amount=total_amount,
                quantity=quantity
           )
        else:
             return jsonify({"status": 400, "message": "Mandatory field empty"})
                 
        if stockId:
            return jsonify({"status" : 200,"message" : stockId})
        else:
            return jsonify({"status" : 400 ,"message":"Something went wrong."})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
def validate_history_data(user_id,product_id,product_name,user_name,quantity,remaining_stock,price,product_category,date_of_sell,total_amount):
    if not user_id or not product_id or not product_name or not user_name or not quantity or not remaining_stock or not price or not product_category or not date_of_sell or not total_amount:
        return 0
    else:
         return 1

@app.route('/getAllSellHistory',methods=['GET'])
def getAllSellHistoryOperation():
    return getAllSellHistoryItem()


@app.route('/getSpecificSellHistory',methods=['POST'])
def getSpecificSellHistoryProduct():
    try:
          sellId = request.form['sell_id']
          getSellHistoryInfo = getSpecificSellHistoryItem(sell_id=sellId)
          return getSellHistoryInfo
     
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})

@app.route('/updateSellHistory',methods=['PATCH'])
def updateSellHistoryItem():
    try:
        sellId = request.form['sell_id']

        allFields = request.form.items()
        updateSellItem = {}

        for key,value in allFields:
                    if key != 'sell_id':
                            updateSellItem[key] = value

        isUpdated = updateSellHistoryItemFields(sellId,**updateSellItem)
        if(isUpdated):  
            return jsonify({"status":200,"message":"Sell history updated Successfull"})
        else:
            return jsonify({"status":400,"message":"Sell Id not found!"})
                          
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})

@app.route('/deleteSellHistory',methods=['DELETE'])
def deleteSellHistoryOperation():
    try:
          sell_id = request.form['sell_id']
          isDeleted = deleteSellHistroyItem(sell_Id=sell_id)

          if(isDeleted):  
                return jsonify({"status":200,"message":"History Sell item Deleted Successfully"})
          else:
                return jsonify({"status":400,"message":"Sell Id not found!"})
     
    except Exception as e:
          return jsonify({"status":400,"message":str(e)})

if __name__ == "__main__":
    createUserTables()
    createProductTable()
    createHistoryTable()
    createOrderTable()
    createStockTable()
    app.run(debug = True)
