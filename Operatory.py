#Zadanie 1
def imie_nazwisko(name, surname):
    return f"Cześć {name}, {surname}"

wynik = imie_nazwisko("Jan", "Kowalski")
print(wynik)
#Zadanie 2
def mnozenie(a, b):
    return a * b
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
wynik = mnozenie(a, b)
print (f"Wynik mnożenia liczby {a} oraz {b} wynosi: {wynik}")
