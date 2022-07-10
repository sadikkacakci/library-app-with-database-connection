import mysql.connector


def getOgrenciNo():
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select ogrenci_no From students")
    result = cursor.fetchall()
    connection.close()    
    return result