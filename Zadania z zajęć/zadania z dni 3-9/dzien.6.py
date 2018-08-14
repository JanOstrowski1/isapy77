nazwa_pliku="licznik.txt"

try :
    plik = open(nazwa_pliku, "r+")
except:
    plik = open(nazwa_pliku, "w+")

aktualny_stan=plik.read()
if aktualny_stan=="":
    aktualny_stan=1
else:
    aktualny_stan=int(aktualny_stan) +1



plik.seek(0)
aktualny_stan= plik.read()
print("")