plik= open("plik.txt", "r+")

wartosc= int(plik.read()) + 1

licznik=int(wartosc)


plik.write(str(licznik))

print(plik.read(licznik))


print("Otworzono: "+str(licznik)+" razy")


plik.close()