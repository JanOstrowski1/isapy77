import os
import sys
print("Ścieżki wyszukiwania Python: ", sys.path)
print("Aktualny folder roboczy: ", os.getcwd())
try:
    os.mkdir("Randomowy plik")
except FileExistsError :
    print("Podany katalog już istenieje ")
os.rmdir("Randomowy plik")
