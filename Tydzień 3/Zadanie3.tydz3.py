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
def pamiętnik():
    try :
        x = input("-->")
    except ValueError :
        print("Wpisałeś liczbę z poza zakresu. Spróbuj jeszcze raz ;-) ")
