class Krzeslo(object):
    """
        Obiekt krzesło
    """

    def __init__(self,material,kolor,cena_zl,ilosc_nog=4,producent=None):
        self.material = material
        self.kolor = kolor
        self.ilosc_nog=ilosc_nog
        self.cena_zl=cena_zl
        self.cena_eu=4.3*cena_zl
        self.producent=producent
        self.przedmiot = __class__.__name__
    def ile_kosztuje(self):
        print("Jestem"+ self.przedmiot+ "i koszutje "+ str(self.cena_zl+ "zł"))
    def kurs_euro(self):
        return 4.3
    def __add__(self, other):
        return self.ilosc_nog+ other.ilosc_nog
    def __str__(self):
        if self.producent is None:
            return "Nie wiem czym jestem."
    def __gt__(self, other):
        if self.ilosc_nog > other.ilosc_nog:
            return "Pierwsze krzesło jest większe."
        else:
            return "Drugie krzesło jest większe. "
