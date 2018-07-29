import string
plik = open("plik1.csv", "r+")

baza_znakow = string.ascii_letters + string.digits + string.punctuation
tekst = plik.read()
print("W podanym pliku : ")
for znak in baza_znakow:
    if tekst.count(znak) != 0:
        print(("Znak {}  występuje : {} razy " ).format(znak, tekst.count(znak),))
plik.close()