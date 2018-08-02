
def piramida():
    while True:
        try:
            wyskosc = int(input("Podaj wysokość piramidy : "))
        except ValueError:
            print("Podaj liczbę całkowitą !")
            piramida()
        except :
            print("Podaj liczbę całkowitą!")
            piramida()

        else:
            for i in range(1, (int(wyskosc) * 2), 2):
                stopien = "#" * i
                print(str(stopien.center(int(wyskosc) * 2)))
        break

piramida()