import string

lista_znakow = string.ascii_letters + string.digits + string.punctuation

tekst = input("Podaj tekst : ")
print(tekst)

print("Oto statystyki twojego tekstu : ")
for znak in lista_znakow:
    if tekst.count(znak) != 0 :
        print(("Znak {} występuje: {}").format(znak,tekst.count(znak)))