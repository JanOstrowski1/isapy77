class Zwierze(object):
    def krolestwo(self):
        print("Zwierze")

    pass

class Czlowiek(Zwierze):
    def gatunek(self):
        return __class__.__name__
    def przywitanie(self):
        return "Cześć !"
    pass

class Student(Czlowiek):
    def przywitanie(self):
        return "Hej!!"
    pass
class Profesor(Czlowiek):
    def przywitanie(self):
        return "Dzień dobry."

class Kot(Zwierze):
    def gatunek(self):
        return __class__.__name__
    pass

class Pies(Zwierze):
    def gatunek(self):
        return __class__.__name__
    pass

class Boxer(Pies):
    pass

class Jamnik(Pies):
    pass

student=Student()
print(student.przywitanie())
profesor=Profesor()
print(profesor.przywitanie())
czlowiek=Czlowiek()
print(czlowiek.przywitanie())