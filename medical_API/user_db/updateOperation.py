import sqlite3

def updateUserName(userId , name):

    conn = sqlite3.connect("my_medical_shop.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?",(name,userId))

    conn.commit()
    conn.close()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Update successful. Rows affected:", cursor.rowcount)
        return 1
    else:
        print("No rows were updated. Check if the userId exists.")
        return 0
    
def updateUserAllFields(userId,**ketword):
    try:
     conn = sqlite3.connect("my_medical_shop.db",timeout=10)
     cursor = conn.cursor()
     
     for key,value in ketword.items():
         if key == "name":
                cursor.execute("UPDATE Users SET name = ? WHERE user_id = ?",(value,userId))
         elif key == "password":
                cursor.execute("UPDATE Users SET password = ? WHERE user_id = ?",(value,userId))
         elif key == "email":
                cursor.execute("UPDATE Users SET email = ? WHERE user_id = ?",(value,userId))

     conn.commit()

     # Check if any rows were affected
     if cursor.rowcount > 0:
                print("Update successful. Rows affected:", cursor.rowcount)
                return 1
     else:
                print("No rows were updated. Check if the userId exists.")
                return 0

    except sqlite3.OperationalError as e:
        print("OperationalError:", e)
    finally:
        # Close the connection
     conn.close()

