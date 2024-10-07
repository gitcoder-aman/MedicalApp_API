import sqlite3

def deleteSellHistroyItem(sell_Id):
    conn = sqlite3.connect("sell_history.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Sell_History WHERE sell_id=?",(sell_Id,))        
    conn.commit()
    conn.close()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Sell History Item Deleted successfully. Rows affected:", cursor.rowcount)
        return 1
    else:
        print("No rows were Deleted. Check if the Sell ID doesn't exists.")
        return 0