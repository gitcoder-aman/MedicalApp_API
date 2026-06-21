import uuid
from datetime import date
from db_config import get_connection

def createUser(name, password, phone_number, email, pinCode, address, userImageId):
    conn = get_connection()
    cursor = conn.cursor()

    user_id = "U_" + str(uuid.uuid4())
    data_of_account_creation = date.today()

    cursor.execute("""
        INSERT INTO Users (
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
            address,
            user_image_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, password, 1, data_of_account_creation, False, False,
          name, email, phone_number, pinCode, address, userImageId))

    conn.commit()
    cursor.close()
    conn.close()

    return user_id
