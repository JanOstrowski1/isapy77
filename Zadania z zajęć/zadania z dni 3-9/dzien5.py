slownik = {"imie":["Łukasz","Jan"] , "nazwisko" : ["Kowalski" , "Malinowski"]}

print(slownik["imie"])

slownik["adres"]=["Gdańsk","Sopot"]

print(slownik.items())



for key , lista  in slownik.items():
    print("Klucz:"+ str(key))
    print("Wartości:")
    for wartosc in lista :
        print("-"+wartosc)
    print("-"*10)