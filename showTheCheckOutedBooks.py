import mysql.connector
from pandas import DataFrame

def showTheCheckOutedBooks():
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select kitap_isim From books where kira = 1")

    result = list(cursor.fetchall())
    df = DataFrame(data = result)
    df.columns = ["Kiralanmış"]
    print("--KİRALANMIŞ KİTAPLAR--")
    i = 1
    for book in df["Kiralanmış"].values:
        print(f"{i}- {book}")