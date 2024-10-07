from flask import Flask,jsonify,request
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
from order_db.read_order_operation import getAllOrderItem,getSpecificOrder
from order_db.order_add_operation import addOrderOperation
from order_db.deleteOrderOperation import deleteOrder

from stock_db.createStockTable import createStockTable
from stock_db.readStockOperation import getAllStockItem
from stock_db.addStockOperation import addStockOperation
from stock_db.updateStockOperation import updateStockAllFields
from stock_db.deleteStockOperation import deleteStock

from history_db.createHistoryTable  import createHistoryTable
from history_db.addHistoryOperation import addSellHistoryOperation
from history_db.readHistoryOperation import getAllSellHistoryItem,getSpecificSellHistoryItem
from history_db.deleteSellHistoryOperation import deleteSellHistroyItem
from history_db.updateSalteHistoryOperation import updateSellHistoryItemFields

app = Flask(__name__)   # app is just a variable (create a instance)


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

        if(validate_user(name,password,email)):
                data = createUser(
                name=name,
                password=password,
                phone_number=phone,
                email=email,
                pinCode=pinCode,
                address=address
           )
        else:
             return jsonify({"status": "Invalid User", "message": "Mandatory field empty"})
                 
        if data:
            return jsonify({"status" : 200,"message" : data})
        else:
            return jsonify({"status" : "Invalid User","message":data})
        
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
                return jsonify({"status" : "Invalid User","message":loginData})
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
     
@app.route('/updateUser',methods=['PATCH'])
def updateUserData():
     try:
          userId = request.form['userId']

          allFields = request.form.items()
          updateUser = {}

          for key,value in allFields:
               if key != 'userId':
                    updateUser[key] = value

          isUpdated = updateUserAllFields(userId=userId,**updateUser)

          if(isUpdated):  
                 return jsonify({"status":200,"message":"data updated"})
          else:
                return jsonify({"status":400,"message":"User Id not found!"})
                    
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})

@app.route('/deleteUser',methods=['DELETE'])
def deleteUser():
     try:
          userId = request.form['userId']
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
        image = request.form['product_image']
        power = request.form['product_power']

    
        if(validate_product(name,category,price,stock,expiry_date,rating,description,image,power)):
               product_id = addProductOperation(
                name=name,
                category=category,
                price=price,
                stock=stock,
                expiry_date=expiry_date,
                rating=rating,
                description=description,
                image=image,
                power=power
            )
        else:
             return jsonify({"status": "Invalid Product fields", "message": "Mandatory field empty"})
                 
        if product_id:
            return jsonify({"status" : 200,"message" : product_id})
        else:
            return jsonify({"status" : "Invalid Product fields","message":product_id})
    except Exception as e:
           return jsonify({"status":400,"message":str(e)})      

def validate_product(name,category,price,stock,expiry_date,rating,description,image,power):
    if not name or not category or not price or not stock or not expiry_date or not rating or not description or not image or not power:
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

          for key,value in allFields:
               if key != 'productId':
                    updateProduct[key] = value

          isUpdated = updateProductAllFields(productId,**updateProduct)

          if(isUpdated):  
                 return jsonify({"status":200,"message":"data updated Successfull"})
          else:
                return jsonify({"status":400,"message":"Product Id not found!"})
                    
     except Exception as e:
          return jsonify({"status":400,"message":str(e)})
     
@app.route('/deleteProduct',methods=['DELETE'])
def deleteProductOperation():
     try:
          productId = request.form['productId']
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
        prodcut_category = request.form['product_category']
        user_name = request.form['user_name']
        isApproved = request.form['isApproved']
        quantity = request.form['product_quantity']
        price = request.form['product_price']
        subtotalPrice = request.form['subtotal_price']
        deliveryCharge = request.form['delivery_charge']
        taxCharge = request.form['tax_charge']
        totalPrice = request.form['total_price']
        orderDate = request.form['order_date']

        if(validate_order_data(user_id,product_id,product_name,prodcut_category,user_name,isApproved,quantity,price,subtotalPrice,totalPrice,orderDate)):
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
                product_category=prodcut_category,
                subtotal_price=subtotalPrice,
                tax_charge=taxCharge,
                delivery_charge=deliveryCharge
           )
        else:
             return jsonify({"status": "Invalid Order", "message": "Mandatory field empty"})
                 
        if orderId:
            return jsonify({"status" : 200,"message" : orderId})
        else:
            return jsonify({"status" : "Invalid Order","message":orderId})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
def validate_order_data(user_id,product_id,product_name,prodcut_category,user_name,isApproved,quantity,price,subtotalPrice,totalPrice,orderDate):
    if not user_id or not product_id or not product_name or not user_name or not isApproved or not quantity or not price or not totalPrice or not orderDate or not prodcut_category or not subtotalPrice:
        return 0
    else:
         return 1

@app.route('/getAllOrder',methods=['GET'])
def getAllOrder():
     return getAllOrderItem()


@app.route('/getSpecificOrder',methods=['POST'])
def getSpecificOrderMain():
     try:
          orderId = request.form['order_id']
          getOrderInfo = getSpecificOrder(orderId = orderId)
          return getOrderInfo
     
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
        product_name = request.form['product_name']
        user_name = request.form['user_name']
        certified = request.form['certified']
        stock = request.form['stock']
        price = request.form['price']
        category = request.form['product_category']

        if(validate_stock_data(user_id,product_id,product_name,user_name,certified,stock,price,category)):
            stockId = addStockOperation(
                user_id=user_id,
                user_name=user_name,
                product_id=product_id,
                category=category,
                product_name=product_name,
                certified=certified,
                price=price,
                stock=stock
           )
        else:
             return jsonify({"status": "Invalid User", "message": "Mandatory field empty"})
                 
        if stockId:
            return jsonify({"status" : 200,"message" : "Stock Product added."})
        else:
            return jsonify({"status" : 400 ,"message":"Something went wrong."})
        
    except Exception as e:
        return jsonify({"status":400,"message":str(e)})
    
def validate_stock_data(user_id,product_id,product_name,user_name,certified,stock,price,category):
    if not user_id or not product_id or not product_name or not user_name or not certified or not stock or not price or not category:
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
             return jsonify({"status": "Invalid User", "message": "Mandatory field empty"})
                 
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
