class Samochod(object):
    def __init__(self,marka,model,kolor,cena_zl,silnik):
        self.marka=marka
        self.model=model
        self.kolor=kolor
        self.cena_zl=cena_zl
        self.silnik = silnik

    def __gt__(self, other):
        if self.cena_zl > other.cena_zl:
            return "Pierwszy samochód jest droższy."
        else:
            return "Drugi samochód jest droższy. "





