from decimal import Decimal

def obliczenia():

    koniec = ""
    while koniec != "tak":
        print("wybierz działanie arytmetyczne:")
        print("1. DODAWANIE")
        print("2. ODEJMOWANIE")
        print("3. MNOŻENIE")
        print("4. DZIELENIE")
        #print("5. POTĘGOWANIE")
        #print("6. PIERWIASTKOWANIE")

        try:
            operation = int(input("wybierz działanie (1-4):\n"))
            num1 = input("podaj pierwszą liczbę\n")
            while not (num1.isdigit or num1.isdecimal()):
                num1 = input("podaj pierwszą liczbę\n")
            num2 = input("podaj drugą liczbę\n")
            while not (num2.isdigit() or num2.isdecimal()):
                num2 = input("podaj druga liczbe\n")
            if operation == 1: #DODAWANIE
                dodawanie("wybrałeś dodawanie", num1, num2)
            elif operation == 2: #ODEJMOWANIE
                odejmowanie("wybrałeś odejmowanie", num1, num2)
            elif operation == 3:  #MNOZENIE
                mnozenie("wybrałeś mnozenie", num1, num2)
            elif operation == 4:  # DZIELENIE
                dzielenie("wybrałeś dzielenie", num1, num2)
            else:
                print("podaj poprawną liczbę!!\n")

        except ValueError:
            print("podaj poprawną liczbę!!\n")

        koniec = input("jeśli chcesz zakończyć program napisz 'tak'\n")


def dodawanie(dzialanie_opis, num1, num2):
    print(dzialanie_opis)
    suma = Decimal(num1) + Decimal(num2)
    print(f"suma liczb {num1} i {num2} wynosi: {suma}\n")


def odejmowanie(dzialanie_opis, num1, num2):
    print(dzialanie_opis)
    roznica = Decimal(num1) - Decimal(num2)
    print(f"roznica liczb {num1} i {num2} wynosi: {roznica}\n")


def mnozenie(dzialanie_opis, num1, num2):
    print(dzialanie_opis)
    iloczyn = Decimal(num1) * Decimal(num2)
    print(f"iloczyn liczb {num1} i {num2} wynosi: {iloczyn}\n")


def dzielenie(dzialanie_opis, num1, num2):
    try:
        print(dzialanie_opis)
        iloraz = Decimal(num1) / Decimal(num2)
        print(f"iloraz liczb {num1} i {num2} wynosi: {iloraz}\n")
    except ZeroDivisionError:
        print("nie dziel przez 0\n")


while True:
    obliczenia()