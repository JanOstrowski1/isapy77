class Pojazd(object):
    def __init__(self,marka,model,kolor,cena_zl,silnik="",uruchomienie = "wyłączony",poziom_paliwa=100 ,):
        self.marka=marka
        self.model=model
        self.kolor=kolor
        self.cena_zl=cena_zl
        self.silnik = silnik
        self.uruchomienie=uruchomienie
        self.poziom_paliwa=poziom_paliwa

    def start_pojazdu (self):
        if self.uruchomienie == "uruchomiony":
            self.uruchomienie = "wyłączony"
            self.poziom_paliwa -= 5
            return "Silnik został wyłączony."
        else:
            self.uruchomienie = "uruchomiony"
            self.poziom_paliwa -= 5
            return "Silnik został uruchomiony."

    def dodaj_silnik(self,silnik):
        if self.silnik=="":
            self.silnik=silnik
            return "Dodano silnik :"+ str(silnik.paliwo)
        else:
            return "Pojazd posiada silnik!"

    pass
class Motocykl(Pojazd):
    def czym_jestem(self):
        return "Jestem motocyklem."
    def stan(self):
        if self.uruchomienie == "wyłączony":
            return "Motocykl jest wyłączony."
        else:
            return "Motocykl jest uruchomiony."

    pass

class Samochod(Pojazd):
    def stan(self):
        if self.uruchomienie == "wyłączony":
            return "Samochód jest wyłączony."
        else:
            return "Samochód jest uruchomiony."

    def czym_jestem(self):
        return "Jestem motocyklem."

class Silnik(Samochod,Motocykl):
    def __init__(self,paliwo):
        self.paliwo=paliwo


silnik_m=Silnik("diesel")
motor=Motocykl("Yamaha","XV","czerwony",2100)
print(motor.dodaj_silnik(silnik_m))
print(motor.start_pojazdu())
print(motor.stan())
print(motor.poziom_paliwa)


