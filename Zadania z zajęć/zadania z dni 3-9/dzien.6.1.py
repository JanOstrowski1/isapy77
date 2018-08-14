import csv

with open("adresy.csv", newline="")as csvfile:
    reader = csv.reader(csvfile)
    for row in reader :
         print(row)
writer = csv.writer(csvfile)

lista = list(reader)

klucze =lista[0]
print(klucze)
del lista[0]
print(lista)

for element in lista[0] :




