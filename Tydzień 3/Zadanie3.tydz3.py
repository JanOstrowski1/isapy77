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
daty={}
def pamiętnik():
    try :
        x = int(input("-->"))
    except ValueError :
        print("Podana wartość nie jest liczbą ! Spróbuj ponownie!")
        pamiętnik()
    if x==1:
        wpis =input("Treść wpisu :")
        data=input("Podaj datę wpisu :")
        daty[data]=wpis
        zbiór_wpisów.append(daty)
        pamiętnik()
    if x==2:
        print("Oto dotychczasowe wpisy:")
        print(zbiór_wpisów)
        pamiętnik()
    if x==3:
        try:
            data=input("Podaj datę z której mam wyświetlić posty: ")
            print(daty[data])
            pamiętnik()
        except:
            print("Wpisana data  nie istnieje :-/")
            pamiętnik()


pamiętnik()

