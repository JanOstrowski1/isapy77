class Pamietnik(object):
    def __init__(self,wpis,data):
        self.wpis=wpis
        self.data=data
    def dodawanie_wpisu(self):
        self.wpis=input("Wpisz tutaj treść wpisu:")
        self.data=input("Podaj datę wpisu :")
    def wyswietlenie_wpisu(self):
        print("Data wpisu : " +str(self.data) + "\n" + "Treść wpisu : "+ str(self.wpis)+ "\n")

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
                print("Nie posiadasz wpisów z podanej daty ¯\_(ツ)_/¯")
        pamiętnik()
    if x==4:
        i = 0
        wpis_do_wyswietlenia = zbiór_wpisów[i]
        wpis_do_wyswietlenia.wyswietlenie_wpisu()
        print("Jeśli chcesz wyświetlić następny wpis wpisz : \"n\" \n Jeśli chcesz wyświtlić poprzedni wpis wciśnij \"p\" \n Jeśli chcesz powrócić do Menu wciśnij dowolny inny klawisz :-)")
        while True :
           z=input(" \n -->  ")
           dlugosc_listy=len(zbiór_wpisów)
           if z== "n":
               i+=1
               if i==dlugosc_listy:
                    i=-1
                    wpis_do_wyswietlenia = zbiór_wpisów[i]
                    wpis_do_wyswietlenia.wyswietlenie_wpisu()
               else:
                   wpis_do_wyswietlenia = zbiór_wpisów[i]
                   wpis_do_wyswietlenia.wyswietlenie_wpisu()
           elif z=="p":
               i-=1
               if i == dlugosc_listy:
                   i=-1
                   wpis_do_wyswietlenia = zbiór_wpisów[i]
                   wpis_do_wyswietlenia.wyswietlenie_wpisu()
               else:
                   wpis_do_wyswietlenia = zbiór_wpisów[i]
                   wpis_do_wyswietlenia.wyswietlenie_wpisu()

           else:
               print("Powrót do menu")
               break
        pamiętnik()

    else:
        print("Liczba z poza zasięgu ¯\_(ツ)_/¯")
        pamiętnik()

pamiętnik()