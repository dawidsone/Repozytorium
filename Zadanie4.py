import cv2
obraz_szary = cv2.imread("kotek.jpg", cv2.IMREAD_GRAYSCALE)
if obraz_szary is None:
    print("Błąd: Nie znaleziono pliku. Sprawdź nazwę lub ścieżkę.")
else:
    czy_zapisano = cv2.imwrite("kotek_szary.jpg", obraz_szary)
    if czy_zapisano:
        print("Obraz został zapisany jako 'kotek_szary.jpg'.")
    else:
        print("Błąd: Nie udało się zapisać zdjęcia w szarości.")