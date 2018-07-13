def kwadrat(x):
    print("+"*x)
    for liczba in range(x-2):
        print("+"+" "*(x-2)+"+")
    print("+"*x)
    print("(To jest kwadrat)")

x=int(input("Podaj bok: "))

kwadrat(x)