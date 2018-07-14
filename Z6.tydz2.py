def początek () :
    x=int(input("Podaj pierwszą liczbę : "))

    while y != "DOŚĆ" :
        y=int(y)
        y=input("Podaj kolejną liczbę:")
        if y=="DOŚĆ":
            wynik = x+y
            print("Wynik twojego działania to : " +  str(wynik) )
            print(str(x)+ "+"  + str(y) )



początek()
