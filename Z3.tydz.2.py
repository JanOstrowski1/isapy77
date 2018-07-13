wysokosc=int(input(" Podaj wysokość piramidy : "))
for x in range(0, wysokosc):
    for y in range(0, wysokosc-x-1):
        print(end=" ")
    for z in range(0, 2*x+1):
        print("*", end="")
    print()