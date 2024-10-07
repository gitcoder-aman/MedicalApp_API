import sqlite3

def deleteStock(stockId):
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Stocks WHERE id=?",(stockId,))        
    conn.commit()
    conn.close()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Stock Deleted successfully. Rows affected:", cursor.rowcount)
        return 1
    else:
        print("No rows were Deleted. Check if the Stock ID doesn't exists.")
        return 0