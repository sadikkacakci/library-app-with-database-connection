import mysql.connector
import pandas as pd
from getKitapId import getKitapId
from getOgrenciNo import getOgrenciNo

def rentABook():
    df_kitap_id = pd.DataFrame(data = getKitapId())
    df_kitap_id.columns = ["Kitap Id"]
    df_ogrenci_no = pd.DataFrame(data = getOgrenciNo())
    df_ogrenci_no.columns = ["Ogrenci No"]
    ogrenci_no = input("Öğrenci numarasını giriniz: ")
    kitap_no = input("Kiralamak istediğiniz kitabın numarasını giriniz: ") # str veya int olabilir dikkat et.

    if (ogrenci_no in df_ogrenci_no["Ogrenci No"].values) and (kitap_no in df_kitap_id["Kitap Id"].values):
        connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
        cursor = connection.cursor()
        cursor.execute(f"Select kira From books where kitap_id = {kitap_no}")
        kira_durumu = list(cursor.fetchone())
        kira_durumu = kira_durumu[0]
        if (kira_durumu == "0"):
            cursor.execute(f"Select kitap_isim From books where kitap_id = {kitap_no}")
            kitap_isim = list(cursor.fetchone())
            kitap_isim = kitap_isim[0]
            print("Kiralanan Kitap: ",kitap_isim)
            sql = f"Update students Set kira_durumu = 1, kiralanan_kitap = %s where ogrenci_no = %s"
            values = [kitap_isim,ogrenci_no]
            cursor.execute(sql,values)

            sql = f"Update books Set kira = 1 where kitap_id = %s"
            values = [kitap_no]
            cursor.execute(sql,values)
            try:
                connection.commit()
                print(f"{cursor.rowcount} tane kayıt güncellendi.")
            except mysql.connector.Error as err:
                print("hata", err)
            finally:
                connection.close()
                print("Database bağlantısı kesildi.")
        if (kira_durumu == "1"):
            print("Kitap kiralanmış durumdadır.")