plik = open("plik.txt", "r+")

lista= ["TEKST5\n", "TEKST6\n"]

plik.writelines(lista)

for line in plik:
     print(line, end="")


plik.close()