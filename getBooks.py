import mysql.connector
def getBooks():
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select kitap_isim From books")
    result = cursor.fetchall()
    connection.close()
    return result