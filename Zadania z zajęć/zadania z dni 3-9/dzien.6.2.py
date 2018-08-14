
import csv

with open("adresy.csv", newline="")as csvfile:
    reader = csv.reader(csvfile)
   # for row in reader :
    #     print(row)
    lista = list(reader)
lista_slownikow = []
klucze =lista[0]
print(klucze)
del lista[0]
print(lista)
print()
print()
for wiersz in lista :
    slownik = {}
    i=0
    for kolumna in wiersz:
        klucz= klucze[i]
        slownik[klucz]= kolumna
        i+=1
    lista_slownikow.append(slownik)

print(lista_slownikow)




