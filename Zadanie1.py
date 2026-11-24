import cv2
#Zadanie 1
# Wczytanie obrazu z pliku
image = cv2.imread("kotek.jpg")

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Zadanie 2
