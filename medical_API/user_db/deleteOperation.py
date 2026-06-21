from db_config import get_connection

def deleteUserOperation(userId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Users WHERE user_id = %s", (userId,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Delete User successfully. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were Deleted. Check if the userId exists.")
        return 0
