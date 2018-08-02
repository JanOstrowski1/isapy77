from wspomnienia import Pamietnik

#3) Napisz program który będzie pamiętnikiem. Niech posiada opcje:
 #  - dodawania wpisu do pamiętnika pod określną datą
  # - wyświetlanie wszystkich wpisów z pamiętnika
   #- wyświetlanie wszystkich wpisów dla określonej daty
   #- przeglądanie pojedyńczych wpisów z pamiętnika, opcja: "następny", "poprzedni"

print("Oto twój pamiętnik")
print("Wpisz \"1\" jeśli chcesz dodać nowy wpis")
print("Wpisz \"2\" jeśli chcesz wyświetlić wyświetlić wszysykie wpisy")
print("Wpisz \"3\" jeśli chcesz wyświetlićwpisy z określownej daty" )
print("Wpisz \"4\" jeśli chcesz przeglądać wpisy po koleji ")
zbiór_wpisów=[]
i=1
wpis=Pamietnik("","")
def pamiętnik():
    try :
        x = int(input("-->"))
    except ValueError :
        print("Podana wartość nie jest liczbą ! Spróbuj ponownie!")
        pamiętnik()
    if x==1:
        wpis.dodawanie_wpisu()
        zbiór_wpisów.append(wpis)

        pamiętnik()
    if x==2:
        for element in zbiór_wpisów:
            element.wyswietlenie_wpisu()
        pamiętnik()
    if x==3:
        szukana_data=input("Podaj datę :")
        for element in zbiór_wpisów:
            if element.data == szukana_data:
                element.wyswietlenie_wpisu()
            else:
                "Nie posiadasz wpisów z podanej daty ¯\_(ツ)_/¯"
        pamiętnik()
    if x==4:
        print("wip")
        pamiętnik()
    else:
        print("Liczba z poza zasięgu ¯\_(ツ)_/¯")
        pamiętnik()

pamiętnik()

