import sqlite3
import json

def getAllSellHistoryItem():
    conn = sqlite3.connect("sell_history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from Sell_History")
    sell_history = cursor.fetchall()
    conn.close()

    sellHistoryJson = []

    for sell_history_Item in sell_history:
        tempSellHistoryItem = {
            "id" : sell_history_Item[0],
            "sell_id":sell_history_Item[1],
            "product_id" : sell_history_Item[2],
            "quantity":sell_history_Item[3],
            "remaining_stock":sell_history_Item[4],
            "date_of_sell":sell_history_Item[5],
            "total_amount":sell_history_Item[6],
            "price":sell_history_Item[7],
            "product_name":sell_history_Item[8],
            "product_category":sell_history_Item[9],
            "user_name":sell_history_Item[10],
            "user_id":sell_history_Item[11]
        }
        sellHistoryJson.append(tempSellHistoryItem)
    return json.dumps(sellHistoryJson)

def getSpecificSellHistoryItem(sell_id):
    conn = sqlite3.connect("sell_history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sell_History WHERE sell_id =?",(sell_id,))
    sell_history = cursor.fetchall()
    conn.close()

    sellHistoryJson = []

    for sell_history_Item in sell_history:
        tempSellHistoryItem = {
            "id" : sell_history_Item[0],
            "sell_id":sell_history_Item[1],
            "product_id" : sell_history_Item[2],
            "quantity":sell_history_Item[3],
            "remaining_stock":sell_history_Item[4],
            "date_of_sell":sell_history_Item[5],
            "total_amount":sell_history_Item[6],
            "price":sell_history_Item[7],
            "product_name":sell_history_Item[8],
            "product_category":sell_history_Item[9],
            "user_name":sell_history_Item[10],
            "user_id":sell_history_Item[11]
        }
        sellHistoryJson.append(tempSellHistoryItem)
    return json.dumps(sellHistoryJson)

