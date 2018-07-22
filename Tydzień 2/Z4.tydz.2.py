wiek_psa=float(input("Podaj wiek psa : "))
if wiek_psa<=2:
    wiek_czlowieka=wiek_psa*10.5
else:
    wiek_czlowieka=2*10.5+(wiek_psa-2)*4
print("Twój pies w przeliczeniu na lata ludzkie ma "+ str(wiek_czlowieka)+" lat" )
