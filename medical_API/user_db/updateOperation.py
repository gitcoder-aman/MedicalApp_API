import psycopg2
from db_config import get_connection

def updateUserName(userId, name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Users SET name = %s WHERE user_id = %s",
        (name, userId)
    )
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Update successful. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were updated. Check if the userId exists.")
        return 0


def updateUserAllFields(userId, **keyword):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        field_map = {
            "name":          "name",
            "password":      "password",
            "email":         "email",
            "phone_number":  "phone_number",
            "level":         "level",
            "isApproved":    "isApproved",
            "block":         "block",
            "pinCode":       "pinCode",
            "address":       "address",
            "user_image_id": "user_image_id",
        }

        for key, value in keyword.items():
            if key in field_map:
                cursor.execute(
                    f"UPDATE Users SET {field_map[key]} = %s WHERE user_id = %s",
                    (value, userId)
                )

        conn.commit()

        if cursor.rowcount > 0:
            print("Update successful. Rows affected:", cursor.rowcount)
            return 1
        else:
            print("No rows were updated. Check if the userId exists.")
            return 0

    except psycopg2.OperationalError as e:
        print("OperationalError:", e)
        return 0
    finally:
        if conn:
            cursor.close()
            conn.close()
