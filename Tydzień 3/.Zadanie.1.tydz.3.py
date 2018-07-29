import csv
def tworzenie_tabelki() :
    try :
        with open(input("Podaj nazwę pliku : "), "r+") as csvfile:
            plik = csv.reader(csvfile)
            lista = list(plik)
            lista_wyrazow = []
            e = len(lista) - 1
            for element in lista:
                lista_wyrazow.extend(lista[e])
                e -= 1

            klucze = lista[0]
            najdluzszy_wyraz = max(lista_wyrazow, key=len)

            for x in klucze:
                print("+" + "-" * len(najdluzszy_wyraz), end="")
            print("+")
            for linijka in lista:

                for wyraz in linijka:
                    print("|" + wyraz + " " * (len(najdluzszy_wyraz) - len(wyraz)), end="")
                print("|")
                for x in klucze:
                    print("+" + "-" * len(najdluzszy_wyraz), end="")
                print("+")
    except FileNotFoundError :
        print("Podany plik nie istnieje !")
        tworzenie_tabelki()
    except:
        print("Upss! Wystąpił nie przewidziany błąd ¯\_(ツ)_/¯.")
        tworzenie_tabelki()
tworzenie_tabelki()










