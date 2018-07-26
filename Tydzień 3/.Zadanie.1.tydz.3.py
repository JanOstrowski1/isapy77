import csv

with open("plik1.csv","r+") as csvfile :
    plik = csv.reader(csvfile)

    lista = list(plik)
    lista_wyrazow=[]
    e=len(lista)-1
    for element in lista:
        lista_wyrazow.extend(lista[e])
        e-=1

    klucze = lista[0]
    najdluzszy_wyraz = max(lista_wyrazow, key=len )

    for x in klucze:
        print("+" + "-" * len(najdluzszy_wyraz), end="")
    print("+")
    for linijka in lista :

        for wyraz in linijka:
            print("|"+ wyraz + " "*(len(najdluzszy_wyraz)-len(wyraz)), end="")
        print("|")
        for x in klucze:
            print("+" + "-" * len(najdluzszy_wyraz), end="")
        print("+")










