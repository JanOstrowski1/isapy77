class Silnik(object):
    def __init__(self,paliwo,stan,uruchomienie="wyłączony",poziom_paliwa=100 ,):
        self.paliwo= paliwo
        self.stan= stan
        self.uruchomienie= uruchomienie
        self.poziom_paliwa = poziom_paliwa
    def uruchamianie(self):
        if self.uruchomienie=="uruchomiony":
            self.uruchomienie="wyłączony"
            self.poziom_paliwa-=5
            return "Silnik został wyłączony."
        else:
            self.uruchomienie="uruchomiony"
            self.poziom_paliwa -= 5
            return "Silnik został uruchomiony."






