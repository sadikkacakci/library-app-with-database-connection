import mysql.connector

def addBooks(list):
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    sql = "INSERT INTO books(kitap_id,kitap_isim,yazar,kira) VALUES (%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values)    
    try:
        connection.commit()  
        print("İşleminiz başarıyla tamamlanmıştır.")       
    except mysql.connector.Error as err:
        print(f"Hata: {err}")       
    finally:
        connection.close()
        print("Database bağlantısı kapatıldı.")  
