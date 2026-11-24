import cv2

# 1. Wczytanie dwóch obrazów (mogą to być dwa różne pliki lub ten sam w różnych trybach)
obraz1 = cv2.imread("kotek.jpg", cv2.IMREAD_COLOR)
obraz2 = cv2.imread("kotek_szary.jpg", cv2.IMREAD_COLOR)  # Możesz zmienić na cv2.IMREAD_GRAYSCALE, jeśli chcesz wczytać w odcieniach szarości

if obraz1 is None or obraz2 is None:
    print("Błąd: Nie udało się wczytać jednego z obrazów.")
else:
    # 2. Otwarcie dwóch osobnych okien (muszą mieć różne nazwy!)
    cv2.imshow("Okno 1 - Kolor", obraz1)
    cv2.imshow("Okno 2 - Szary", obraz2)

    okno1_otwarte = True
    okno2_otwarte = True

    # 3. Pętla pozwalająca na niezależne zamykanie każdego okna (myszką lub klawiszem)
    while okno1_otwarte or okno2_otwarte:
        klawisz = cv2.waitKey(50) & 0xFF

        # Obsługa Okna 1 (zamknięcie klawiszem '1' lub krzyżykiem X)
        if okno1_otwarte:
            if klawisz == ord("1"):
                cv2.destroyWindow("Okno 1 - Kolor")
                okno1_otwarte = False
            elif cv2.getWindowProperty("Okno 1 - Kolor", cv2.WND_PROP_VISIBLE) < 1:
                okno1_otwarte = False

        # Obsługa Okna 2 (zamknięcie klawiszem '2' lub krzyżykiem X)
        if okno2_otwarte:
            if klawisz == ord("2"):
                cv2.destroyWindow("Okno 2 - Szary")
                okno2_otwarte = False
            elif cv2.getWindowProperty("Okno 2 - Szary", cv2.WND_PROP_VISIBLE) < 1:
                okno2_otwarte = False

        # Opcjonalnie: klawisz ESC zamyka wszystkie pozostałe okna naraz
        if klawisz == 27:
            cv2.destroyAllWindows()
            break