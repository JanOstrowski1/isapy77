import string
plik = open("plik1.csv", "r+")

baza_znakow = string.ascii_letters + string.digits + string.punctuation
tekst = plik.read()
print("W pliku występuje: ")
for znak in baza_znakow:
    if tekst.count(znak) != 0:
        print(("{} x {}").format(znak, tekst.count(znak)))
plik.close()