import pandas as pd
from getBooks import getBooks

def showTheBooks():
    df = pd.DataFrame(data = getBooks())
    df.columns = ["Kitap İsimleri"]

    i = 1
    print("--KİTAPLAR--")
    for book in df["Kitap İsimleri"].values:
        
        print(f"{i}- {book}")
        i+=1