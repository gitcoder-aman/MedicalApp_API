import sqlite3
import uuid
from datetime import date

def createUser(name,password,phone_number,email,pinCode,address):
   conn = sqlite3.connect("my_medical_shop.db")
   cursor = conn.cursor() 

   user_id = "U_"+str(uuid.uuid4())
   data_of_account_creation = date.today()

   cursor.execute("""
         INSERT INTO Users(
                  user_id,
                  password,
                  level,
                  date_of_account_creation,
                  isApproved,
                  block,
                  name,
                  email,
                  phone_number,
                  pinCode,
                  address) VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """,(user_id,password,1,data_of_account_creation,0,0,name,email,phone_number,pinCode,address))
   
   conn.commit()
   conn.close()

   return user_id
