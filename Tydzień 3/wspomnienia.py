class Pamietnik(object):
    def __init__(self,wpis,data):
        self.wpis=wpis
        self.data=data
    def dodawanie_wpisu(self):
        self.wpis=input("Wpisz tutaj treść wpisu:")
        self.data=input("Podaj datę wpisu :")
    def wyswietlenie_wpisu(self):
        print("Data wpisu : " +str(self.data) + "\n" + "Treść wpisu : "+ str(self.wpis)+ "\n")

