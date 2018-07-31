import string
znaki = string.ascii_letters + string.digits + string.punctuation
def statystyki_tekstu() :
    try :
        plik = open(input("Podaj nazwę pliku : "), "r+")

    except FileNotFoundError :
        print("Podany plik nie istnieje !")
        statystyki_tekstu()
    except:
        print("Upss! Wystąpił nie przewidziany błąd ¯\_(ツ)_/¯.")
        statystyki_tekstu()
    tekst = plik.read()
    print("W podanym pliku : ")
    for znak in znaki:
        if tekst.count(znak) != 0:
            print(("Znak {}  występuje : {} razy ").format(znak, tekst.count(znak), ))
    plik.close()
statystyki_tekstu()

