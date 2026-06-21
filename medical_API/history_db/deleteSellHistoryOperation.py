from db_config import get_connection

def deleteSellHistroyItem(sell_Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Sell_History WHERE sell_id = %s", (sell_Id,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Sell History Item Deleted successfully. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were Deleted. Check if the Sell ID doesn't exists.")
        return 0