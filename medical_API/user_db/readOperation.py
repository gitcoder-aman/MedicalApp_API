import sqlite3
import json

def getAllUsers():
    conn = sqlite3.connect("my_medical_shop.db")
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()

    # print(users)

    userJson = []

    for user in users:
        tempUser = {
            "id" : user[0],
            "user_id" : user[1],
            "password" : user[2],
            "level" : user[3],
            "date_of_account_creation" : user[4],
            "isApproved" : user[5],
            "block" : user[6],
            "name" : user[7],
            "email" : user[8],
            "phone_number" : user[9],
            "pinCode" : user[10],
            "address" : user[11]
        }
        
        userJson.append(tempUser)

    return json.dumps(userJson)
        # print(json.dumps(userJson))
        
# getAllUsers()

def getSpecificUser(userId):
    conn = sqlite3.connect("my_medical_shop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE user_id =?",(userId,))
    users = cursor.fetchall()
    conn.close()

    userJson = []

    for user in users:
        tempUserSpecific = {
            "id" : user[0],
            "user_id" : user[1],
            "password" : user[2],
            "level" : user[3],
            "date_of_account_creation" : user[4],
            "isApproved" : user[5],
            "block" : user[6],
            "name" : user[7],
            "email" : user[8],
            "phone_number" : user[9],
            "pinCode" : user[10],
            "address" : user[11]
        }
        
        userJson.append(tempUserSpecific)

    return json.dumps(userJson)