from db_config import get_connection

def deleteStock(stockId):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Stocks WHERE id = %s", (stockId,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()

    if rows_affected > 0:
        print("Stock Deleted successfully. Rows affected:", rows_affected)
        return 1
    else:
        print("No rows were Deleted. Check if the Stock ID doesn't exists.")
        return 0