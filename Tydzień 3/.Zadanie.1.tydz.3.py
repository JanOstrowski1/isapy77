#1) Stwórz program który przyjmie w parametrze ścieżkę do dowolnego pliku CSV który będzie zawierał dane tabelaryczne.
 #  W pliku pierwszy wiersz będzie zawierał nazwy kolumn a pozostałe wiersze dane. Ilość kolum i wierszy może być dowolna.
  # Program ma narysować tabelę z danymi, analogicznie do zadania nr 1 z dnia 4.
   #Atutem będzie wydzielenie części reużywalnych do oddzielnych metod (np.: odczyt danych, przygotowanie danych, rysowanie tabeli)
   #+------------+------------+------------+
   #| klucz1     | klucz 2    | klucz 3    |
   #+------------+------------+------------+
   #| row 1 col1 | row 1 col2 | row 1 col3 |
   #+------------+------------+------------+
   #| row 2 col1 | row 2 col2 | row 2 col3 |
   #+------------+------------+------------+


import csv

with open("plik1.csv","r+") as csvfile :
    plik = csv.reader(csvfile)

    lista = list(plik)
    lista_wyrazow=[]
    e=len(lista)-1
    for element in lista:
        lista_wyrazow.append(lista[e])
        e-=1

    klucze = lista[0]
    najldluzszy_argument = max(lista_wyrazow, key=len )
    najdluzszy_wyraz = max(najldluzszy_argument, key=len)

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










