from getBooks import getBooks


def searchBookByName():
    text = input("Aradığınız kitabın adını giriniz: ")
    books = getBooks()
    result = False
    for book in books:
        if text in book:
            result = True
            break
    if result == True:
        print(f"{text} mevcut.")
    else:
        print("Kitap mevcut değil.")