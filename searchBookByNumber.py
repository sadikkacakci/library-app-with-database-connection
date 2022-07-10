import mysql.connector
from pandas import DataFrame
def searchBookByNumber():
    number = input("Kitap id'sini giriniz: ")
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select kitap_id From books")
    kitap_idies = cursor.fetchall()
    df = DataFrame(data = kitap_idies)
    df.columns = ["Kitap Id"]
    if number in df["Kitap Id"].values:
        cursor.execute(f"Select kitap_isim From books where kitap_id = {number}")
        kitap_isim = list(cursor.fetchone())
        kitap_isim = kitap_isim[0]
        print(kitap_isim)
    else:
        print("Bu numaraya ait bir kitap bulunmamaktadır.")