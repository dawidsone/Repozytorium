import cv2

# 1. Wczytanie obrazu w odcieniach szarości
obraz = cv2.imread("kotek.jpg", cv2.IMREAD_GRAYSCALE)

if obraz is None:
    print("Błąd: Nie znaleziono pliku. Sprawdź nazwę lub ścieżkę.")
else:
    # 2. Obraz w skali szarości ma 2 wymiary (wysokość, szerokość), co oznacza 1 kanał
    kanaly = 1 if obraz.ndim == 2 else obraz.shape[2]
    print(f"Liczba kanałów: {kanaly}")

    cv2.imshow("Obraz w odcieniach szarości", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()