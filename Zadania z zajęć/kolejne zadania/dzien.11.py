class Produkt(object):
    kurs_euro= 4.3
    def __init__(self,nazwa,cena,producent="Nie  znany"):
        self.nazwa = nazwa
        self.cena = cena
        self.producent = producent
    @staticmethod
    def pobierz_kurs_euro():
        return "1 EURO= " + str(Produkt.kurs_euro) + "PLN"

    def pobierz_producenta(self):
        if self.producent== "Chiny":
            return "Świat"
        else:
            return self.producent



    @classmethod
    def dlugopis(cls):
        return cls("dlugopis",1,"Chiny")

    @classmethod
    def linijka(cls):
        return cls("linijka",1.5)

    def jaka_cena(self):
        return self.nazwa + " kosztuje " + str(self.cena)
    @property
    def nazwa(self):
        return "Moja nazwa to: " + self.nazwa
    @nazwa.setter
    def nazwa(self,nowa_nazwa):
        self.nazwa = nowa_nazwa.capitalize()
    print("Właśnie zmieniono nazwę.")
    @nazwa.deleter
    def nazwa(self):
        self.nazwa="BRAK"

print(Produkt.pobierz_kurs_euro())
ekierka = Produkt("ekierka",2)
print(ekierka.jaka_cena())
dlugopis = Produkt.dlugopis()
print(dlugopis.jaka_cena())
print(dlugopis.pobierz_producenta())

print(Produkt.__dict__)