parametr=int(input("Wybierz działanie :Dodawanie=1 , Odejmowanie=2 , Mnożenie =3, Dzielenie=4, "))
def dzialanie(x,y) :
    if parametr == 1:
        print("Wynik dodawania to:")
        print(x+y)

    if parametr == 2:
        print("Wynik odejmowania to:")
        print(x-y)
    if parametr == 3:
        print("Wynik mnożenia to :")
        print(x*y)
    if parametr == 4 :
        print("wynik dzielenia to:")
        print(x/y)

x=int(input("Podaj x :"))
y=int(input("Podaj y : "))

dzialanie(x,y)







