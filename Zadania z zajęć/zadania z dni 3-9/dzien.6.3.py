import pickle
lista = [1,2,3,4]
with  open("plik_do_6.3.txt", "wb") as plik :
    pickle.dump(lista,plik)
