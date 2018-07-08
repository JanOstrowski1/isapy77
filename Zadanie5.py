prosta = "-"
wierzcholek = "*"
prosta_pionowa = "|"
puste_pole=" "
dlugosc_a= input("Podaj dlugosc boku a : ")
dlugosc_b=input("Podaj długość boku b : ")
wartosc_a=int(dlugosc_a)
wartosc_b=int(dlugosc_b)
print(wierzcholek+prosta*wartosc_a +wierzcholek )
 if(wartosc_b>1 , print(prosta_pionowa+puste_pole*wartosc_a+prosta_pionowa), wartosc_b= wartosc_b -1 )