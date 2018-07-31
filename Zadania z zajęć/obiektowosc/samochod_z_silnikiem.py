from samochod import Samochod
from silnik import Silnik
silnik = Silnik("benzyna","dobry")
silnik2 = Silnik("diesel","średni")
moj_samochod=Samochod("Audi","a4","czarny",50000,silnik)

moj_samochod2=Samochod("Mazda","6","czerwony",100000,silnik2)
print(moj_samochod.silnik.poziom_paliwa)
print(moj_samochod.silnik.uruchomienie)
moj_samochod.silnik.uruchamianie()
print(moj_samochod.silnik.uruchomienie)
print(moj_samochod.silnik.poziom_paliwa)