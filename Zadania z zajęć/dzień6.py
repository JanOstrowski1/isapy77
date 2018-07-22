import csv

with open("plik1.csv",) as csvfile :
    plik = csv.reader(csvfile)

    lista = list(plik)
    klucze = lista[0]
    del lista[0]
    lista_slownikow = []
    for wiersz in lista:
        slownik = {}
        i = 0
        for kolumna in wiersz:
            klucz = klucze[i]
            slownik[klucz] = kolumna
            i += 1
        lista_slownikow.append(slownik)

    print(lista_slownikow)
    print()





