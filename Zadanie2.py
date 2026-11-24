import cv2

# 1. Wczytanie zdjęcia w kolorze
obraz = cv2.imread("kotek.jpg", cv2.IMREAD_COLOR)

# Zabezpieczenie na wypadek literówki w nazwie pliku
if obraz is None:
    print("Błąd: Nie znaleziono pliku. Sprawdź nazwę lub ścieżkę.")
else:
    # 2. obraz.shape zwraca krotkę: (wysokość, szerokość, liczba_kanałów)
    wysokosc, szerokosc, kanaly = obraz.shape
    print(f"Liczba kanałów: {kanaly}")