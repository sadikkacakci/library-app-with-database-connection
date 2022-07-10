import mysql.connector

def getKitapId():
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select kitap_id From books")
    result = cursor.fetchall()
    connection.close()
    return result
