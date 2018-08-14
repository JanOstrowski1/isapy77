

#lista=["a","b","c",["1","2","3"]]

#nowa_lista = lista
#kopia_listy =copy.copy(lista)
#gleboka_kopia_listy=copy.deepcopy(lista)
#nowa_lista[3][0] = "x"
#kopia_listy[3][0] = "y"
#gleboka_kopia_listy[3][0]="z"

#print(lista)
#print(nowa_lista)
#print(kopia_listy)
#print(gleboka_kopia_listy)


def dodawanie(x,y):
    print(x+y)

liczba_x=input("Podaj x:")
liczba_y=input("Podaj y:")
x=int(liczba_x)
y=int(liczba_y)



print("Twój wynik to:" ) , dodawanie(x,y)


