import mysql.connector
import pandas as pd

def showTheStudents():
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "kütüphane")
    cursor = connection.cursor()
    cursor.execute("Select ogrenci_isim From students")
    result = cursor.fetchall()
    connection.close()
    result
    df = pd.DataFrame(data = result)
    df.columns = ["Öğrenci İsimleri"]

    i = 1
    print("--ÖĞRENCİLER--")
    for student in df["Öğrenci İsimleri"].values:
        print(f"{i}- {student}")
        i+=1
