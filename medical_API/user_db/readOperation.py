import json
from db_config import get_connection

def _row_to_user(user):
    return {
        "id":                       user[0],
        "user_id":                  user[1],
        "password":                 user[2],
        "level":                    user[3],
        "date_of_account_creation": str(user[4]),
        "isApproved":               user[5],
        "block":                    user[6],
        "name":                     user[7],
        "email":                    user[8],
        "phone_number":             user[9],
        "pinCode":                  user[10],
        "address":                  user[11],
        "user_image_id":            user[12],
    }

def getAllUsers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_user(u) for u in users])

def getSpecificUser(userId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE user_id = %s", (userId,))
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return json.dumps([_row_to_user(u) for u in users])