from showTheBooks import showTheBooks
from showTheCheckOutedBooks import showTheCheckOutedBooks
from addBooks import addBooks
from searchBookByNumber import searchBookByNumber
from searchBookByName import searchBookByName
from rentABook import rentABook
from showTheStudents import showTheStudents

def menu():
    while True:
        print("****MENU****")
        choice = int(input("1-Show The Books\n2-Show The Check Outed Books\n3-Add A Book\n4-Search Book By ISBN Number\n5-Search Book By Name\n6-Rent A Book\n7-Show The Students\n8-Quit\nSeçim:"))
        if choice == 1:
            showTheBooks()
        elif choice == 2:
            showTheCheckOutedBooks()
        elif choice == 3:
            from random import randint
            liste = []
            while True:
                kitap_isim = input("Kitap ismini giriniz: ")
                yazar = input("Yazar ismini giriniz: ")
                kitap_id = randint(1000000000,9999999999)
                liste.append((kitap_id,kitap_isim,yazar,0))
                result = int(input("Başka kitap eklemek istiyor musunuz? 1-Evet  2-Hayır\nSeçim:"))
                if result == 2:
                    addBooks(liste)
                    print("Kayıtlarınız veritabanına aktarılıyor.")
                    break
        elif choice == 4:
            searchBookByNumber()
        elif choice == 5:
            searchBookByName()
        elif choice == 6:
            rentABook()
        elif choice == 7:
            showTheStudents()
        elif choice == 8:
            print("İyi Günler.")
            break
        else:
            print("Hatalı giriş yaptınız.")

