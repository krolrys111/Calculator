def obliczenia():

    print("wybierz działanie arytmetyczne:")
    print("1. DODAWANIE")
    print("2. ODEJMOWANIE")
    print("3. MNOŻENIE")
    print("4. DZIELENIE")
    print("5. POTĘGOWANIE")
    print("6. PIERWIASTKOWANIE")

    try:
        operation = int(input("wybierz działanie (1-6):\n"))
        if operation == 1: #DODAWANIE
            print("wybrałeś dodawanie")
            num1 = input("podaj pierwszą liczbę\n")
            num2 = input("podaj drugą liczbę\n")
            suma = float(num1) + float(num2)
            print(f"suma liczb {num1} i {num2} wynosi: {suma}\n")
        elif operation == 2: #ODEJMOWANIE
            print("wybrałeś odejmowanie")
            num1 = input("podaj pierwszą liczbę\n")
            num2 = input("podaj drugą liczbę\n")
            roznica = float(num1) - float(num2)
            print(f"różnica liczb {num1} i {num2} wynosi: {roznica}\n")
        elif operation == 3: #MNOŻENIE
            print("wybrałeś mnożenie")
            num1 = input("podaj pierwszą liczbę\n")
            num2 = input("podaj drugą liczbę\n")
            iloczyn = float(num1) * float(num2)
            print(f"iloczyn liczb {num1} i {num2} wynosi: {iloczyn}\n")
        elif operation == 4: #DZIELENIE
            print("wybrałeś dzielenie")
            num1 = input("podaj pierwszą liczbę\n")
            num2 = input("podaj drugą liczbę\n")
            iloraz = float(num1) / float(num2)
            print(f"iloraz liczb {num1} i {num2} wynosi: {iloraz}\n")
        elif operation == 5: #POTĘGOWANIE
            print("wybrałeś potęgowanie")
            num1 = input("podaj liczbę\n")
            num2 = input("do której potęgi\n")
            potega = float(num1) ** float(num2)
            print(f"liczba {num1} do potęgi {num2} wynosi: {potega}\n")
        elif operation == 6: #PIERWIASTKOWANIE
            print("wybrałeś pierwiastkowanie")
            num1 = input("podaj liczbę\n")
            num2 = int(input("pierwiastek którego stopnia\n"))
            roott = float(1. / num2)
            pierwiastek = float(num1) ** roott
            print(f"pierwiastek {num2} stopnia liczby {num1} wynosi: {pierwiastek}\n")
        else:
            print("podaj poprawną liczbę!!\n")

    except ValueError:
        print("podaj poprawną liczbę!!\n")

while True:
    obliczenia()