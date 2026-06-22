from db_config import get_connection

def createUserTables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id               SERIAL PRIMARY KEY,
            user_id          VARCHAR(255),
            password         VARCHAR(255),
            level            INT,
            date_of_account_creation DATE,
            isApproved       BOOLEAN,
            block            BOOLEAN,
            name             VARCHAR(255),
            email            VARCHAR(255),
            phone_number     VARCHAR(255),
            pinCode          VARCHAR(255),
            address          VARCHAR(255),
            user_image_id    TEXT
        )
    """)

    # Fix existing table if column was already created as VARCHAR(20)
    # Cloudinary URLs are ~100+ chars and won't fit in VARCHAR(20)
    cursor.execute("""
        ALTER TABLE Users
        ALTER COLUMN user_image_id TYPE TEXT
    """)

    conn.commit()
    cursor.close()
    conn.close()
