kwota = int(input("Podaj kwotę (w groszach):"))
l_piątek=0
l_dwójek=0
l_jedynek=0
l_50_groszówek=0
l_20_groszówek=0
l_10_groszówek=0

while kwota>=500:
    l_piątek+=1
    kwota-=500
while kwota>=200:
    l_dwójek+=1
    kwota-=200
while kwota>=100:
    l_jedynek+=1
    kwota-=100
while kwota>=50:
    l_50_groszówek+=1
    kwota-=50
while kwota>=20:
    l_20_groszówek+=1
    kwota-=20
while kwota>=10:
    l_10_groszówek+=1
    kwota-=10

if l_piątek>0:
    print("Otrzymujesz od automatu: " + str(l_piątek) + " piątek")
if l_dwójek>0:
    print("Otrzymujesz od automatu: " + str(l_dwójek) + " dwójek")
if l_jedynek>0:
    print("Otrzymujesz od automatu: " + str(l_jedynek) + " jedynek")
if l_50_groszówek>0:
    print("Otrzymujesz od automatu: " + str(l_50_groszówek) + " pięćdziesięciogroszówek")
if l_20_groszówek>0:
    print("Otrzymujesz od automatu: " + str(l_20_groszówek) + " dwódziestogroszówek")
if  l_10_groszówek>0:
    print("Otrzymujesz od automatu: " + str(l_10_groszówek) + " dziesięciogroszówek")

if kwota > 0:
    print("Automat nie wydaje mniejszych drobnych ;-) .")
