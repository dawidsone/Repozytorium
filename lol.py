print("Witam")
print("Wersja test")
print("Konflikt test")
print("Ten program pozwala wprowadzać liczby i je wyświetlać.")
while True:
    user_input = input("Podaj liczbę (lub wpisz 'exit' aby zakończyć): ")
    if user_input.lower() == 'exit':
        print("Koniec programu.")
        break
    try:
        number = float(user_input)
        print(f"Wprowadziłeś liczbę: {number}")
    except ValueError:
        print("To nie jest prawidłowa liczba. Spróbuj ponownie.")