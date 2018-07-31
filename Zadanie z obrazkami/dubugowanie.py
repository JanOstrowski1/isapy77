dni_tygodnia=["poniedziałek","wtorek","środa","czwartek","piętek","sobota","niedziela"]
weekend= ["sobota","niedziela"]
for dzien in dni_tygodnia:
    if dzien in weekend:
        print(" {} :To jest weekend".format(dzien))
    else:
        print("{}: Pracujemy dalej".format(dzien))
