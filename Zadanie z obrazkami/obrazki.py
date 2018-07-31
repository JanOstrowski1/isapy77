import requests

from bs4 import BeautifulSoup

url= "https://wallpaperlist.com/"

strona = requests.get(url)

zrodlo_strony = strona.content

soup = BeautifulSoup(zrodlo_strony, "html.parser")


for item in soup.find_all("img"):
    nazwa_pliku= item["src"].split("/")[-1]
    adres_do_obrazka = url + item["src"]
    obrazek =requests.get(adres_do_obrazka).content

    plik = open("obrazki"+nazwa_pliku,"wb+")
    plik.write(obrazek)
    plik.close()
