import pygame
import os
import time
import winsound
import threading

class MenedzerDzwiekowWinsound:
    def __init__(self):
        pass

    def odtworz_pudlo(self):
        def _graj():
            winsound.Beep(400, 80)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

    def dzwiek(self, czestotliwosc, czas):
        def _graj():
            winsound.Beep(czestotliwosc, czas)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

class gra:
    def __init__(self, nutki):
        self.nutki = nutki
        self.state = "start"
        self.dzwieki = MenedzerDzwiekowWinsound()
        self.screen = None

    def wczytaj_piosenke(self):
        # Parametr 'dlugosc_trwania' określa, ile sekund trwa nuta na ekranie (np. 0.4 sekundy dla dłuższej nuty)
        # Parametr 'czas_trwania' to czas trwania dźwięku w ms (np. 350 ms)
        
        self.nutki.append(nuta(kolumna=2, czas=2.00, czestotliwosc=659, czas_trwania=250, dlugosc_trwania=0.3))  # E5 (dłuższa)
        self.nutki.append(nuta(kolumna=2, czas=2.50, czestotliwosc=659, czas_trwania=150, dlugosc_trwania=0.15)) # E5 (krótka)
        self.nutki.append(nuta(kolumna=2, czas=3.00, czestotliwosc=659, czas_trwania=150, dlugosc_trwania=0.15)) # E5
        self.nutki.append(nuta(kolumna=1, czas=3.33, czestotliwosc=523, czas_trwania=150, dlugosc_trwania=0.15)) # C5
        self.nutki.append(nuta(kolumna=2, czas=3.66, czestotliwosc=659, czas_trwania=250, dlugosc_trwania=0.3))  # E5 (dłuższa)
        self.nutki.append(nuta(kolumna=4, czas=4.33, czestotliwosc=784, czas_trwania=300, dlugosc_trwania=0.35)) # G5
        self.nutki.append(nuta(kolumna=3, czas=5.33, czestotliwosc=392, czas_trwania=300, dlugosc_trwania=0.35)) # G4

        self.nutki.append(nuta(kolumna=1, czas=6.66, czestotliwosc=523, czas_trwania=200, dlugosc_trwania=0.2))
        self.nutki.append(nuta(kolumna=3, czas=7.33, czestotliwosc=392, czas_trwania=200, dlugosc_trwania=0.2))
        self.nutki.append(nuta(kolumna=2, czas=8.00, czestotliwosc=330, czas_trwania=200, dlugosc_trwania=0.2))
        self.nutki.append(nuta(kolumna=3, czas=8.66, czestotliwosc=440, czas_trwania=150, dlugosc_trwania=0.15))
        self.nutki.append(nuta(kolumna=4, czas=9.00, czestotliwosc=494, czas_trwania=150, dlugosc_trwania=0.15))
        self.nutki.append(nuta(kolumna=3, czas=9.33, czestotliwosc=466, czas_trwania=150, dlugosc_trwania=0.15))
        self.nutki.append(nuta(kolumna=2, czas=9.66, czestotliwosc=440, czas_trwania=200, dlugosc_trwania=0.2))

        self.nutki.append(nuta(kolumna=3, czas=10.33, czestotliwosc=784, czas_trwania=200, dlugosc_trwania=0.2))
        self.nutki.append(nuta(kolumna=2, czas=10.66, czestotliwosc=659, czas_trwania=200, dlugosc_trwania=0.2))
        self.nutki.append(nuta(kolumna=1, czas=11.00, czestotliwosc=523, czas_trwania=150, dlugosc_trwania=0.15))
        self.nutki.append(nuta(kolumna=2, czas=11.33, czestotliwosc=587, czas_trwania=150, dlugosc_trwania=0.15))
        self.nutki.append(nuta(kolumna=4, czas=11.66, czestotliwosc=494, czas_trwania=250, dlugosc_trwania=0.25))

    def rysuj_planszę(self):
        self.screen.fill((0, 0, 0))
        BIALY = (255, 255, 255)
        ZIELONY = (0, 255, 0)
        ZOLTY = (255, 255, 0)
        szerokosc_kolumny = 100
       
        for i in range(1, 4):
            x = i * szerokosc_kolumny
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, 600), 2)

        y_uderzenia = 500
        pygame.draw.line(self.screen, BIALY, (0, y_uderzenia), (400, y_uderzenia), 4)

        aktualny_czas = pygame.time.get_ticks() / 1000.0
        skala_y = y_uderzenia / 2.0  # 2 sekundy = 500 pikseli

        for n in self.nutki:
            czas_do_uderzenia = n.czas - aktualny_czas
            
            # Widzimy nutę, jeśli jej koniec lub początek mieści się w oknie
            if -1.0 <= czas_do_uderzenia <= 2.5:
                # Pozycja Y górnej krawędzi nuty
                y_pozycja = y_uderzenia - (czas_do_uderzenia * skala_y)
                
                # Wysokość prostokąta w pikselach zależna od czasu trwania nuty
                wysokosc_nuty = n.dlugosc_trwania * skala_y
                
                # Przesuwamy prostokąt w górę, aby rósł "w tył" od punktu uderzenia
                y_pozycja_prostokata = y_pozycja - wysokosc_nuty

                x_pozycja = (n.kolumna - 1) * szerokosc_kolumny + (szerokosc_kolumny // 2) - 15
                
                kolor_nuty = ZOLTY if n.trafiona else ZIELONY
                
                # Rysujemy nutę jako dłuższy prostokąt (paski zamiast małych kwadratów)
                pygame.draw.rect(self.screen, kolor_nuty, (x_pozycja, y_pozycja_prostokata, 30, max(int(wysokosc_nuty), 10)))

        pygame.display.flip()

    def sprawdz_wejscie(self, kolumna):
        aktualny_czas = pygame.time.get_ticks() / 1000.0
        okno_trafienia = 0.15  # tolerancja w sekundach (ok. 150 ms)

        for n in self.nutki:
            if n.kolumna == kolumna and not n.trafiona:
                roznica = abs(n.czas - aktualny_czas)
                
                if roznica <= okno_trafienia:
                    n.trafiona = True
                    print("Trafienie! (Hit)")
                    self.dzwieki.dzwiek(n.czestotliwosc, n.czas_trwania)
                    return

        print("Pudło!")
        self.dzwieki.odtworz_pudlo()

    def uruchom(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.sprawdz_wejscie(1)
                    elif event.key == pygame.K_2:
                        self.sprawdz_wejscie(2)
                    elif event.key == pygame.K_3:
                        self.sprawdz_wejscie(3)
                    elif event.key == pygame.K_4:
                        self.sprawdz_wejscie(4)
                        
            self.rysuj_planszę()

class nuta:
    def __init__(self, kolumna, czas, czestotliwosc=440, czas_trwania=200, dlugosc_trwania=0.15):
        self.kolumna = kolumna
        self.czas = czas
        self.trafiona = False
        self.aktywna = False
        self.czestotliwosc = czestotliwosc      # Ton dźwięku w Hz
        self.czas_trwania = czas_trwania        # Czas trwania Beep w ms
        self.dlugosc_trwania = dlugosc_trwania  # Czas trwania nuty na ekranie w sekundach

if __name__ == "__main__":
    gra1 = gra([])
    gra1.wczytaj_piosenke()

    try:
        gra1.uruchom()
    except KeyboardInterrupt:
        print("\nGra została przerwana. Do zobaczenia!")