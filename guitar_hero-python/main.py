import pygame
import os
import time
import winsound
import threading

class MenedzerDzwiekowWinsound:
    def __init__(self):
        pass

    def odtworz_pudlo(self):
        """Odtwarza krótki, ostrzegawczy dźwięk pudła w osobnym wątku."""
        def _graj():
            winsound.Beep(400, 80)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

    def dzwiek(self, czestotliwosc, czas):
        """Odtwarza konkretną nutę melodii w osobnym wątku."""
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
        # Przypisujemy każdej nucie unikalną częstotliwość i czas trwania dźwięku
        self.nutki.append(nuta(kolumna=1, czas=2.0, czestotliwosc=262, czas_trwania=150))  # C4
        self.nutki.append(nuta(kolumna=2, czas=2.5, czestotliwosc=294, czas_trwania=150))  # D4
        self.nutki.append(nuta(kolumna=3, czas=3.0, czestotliwosc=330, czas_trwania=150))  # E4
        self.nutki.append(nuta(kolumna=4, czas=3.5, czestotliwosc=349, czas_trwania=150))  # F4
        self.nutki.append(nuta(kolumna=2, czas=4.5, czestotliwosc=392, czas_trwania=150))  # G4
        self.nutki.append(nuta(kolumna=1, czas=5.0, czestotliwosc=440, czas_trwania=200))  # A4

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
        for n in self.nutki:
            czas_do_uderzenia = n.czas - aktualny_czas
            
            if -0.5 <= czas_do_uderzenia <= 2.0:
                y_pozycja = y_uderzenia - (czas_do_uderzenia * (y_uderzenia / 2.0))
                x_pozycja = (n.kolumna - 1) * szerokosc_kolumny + (szerokosc_kolumny // 2) - 15
                
                kolor_nuty = ZOLTY if n.trafiona else ZIELONY
                pygame.draw.rect(self.screen, kolor_nuty, (x_pozycja, y_pozycja, 30, 15))

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
                    # Odtwarzamy dźwięk przypisany do tej konkretnej nuty
                    self.dzwieki.dzwiek(n.czestotliwosc, n.czas_trwania)
                    return

        # Jeśli pętla sprawdziła kolumnę i nie znalazła nuty w oknie trafienia -> Pudło!
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
    def __init__(self, kolumna, czas, czestotliwosc=440, czas_trwania=200):
        self.kolumna = kolumna
        self.czas = czas
        self.trafiona = False
        self.aktywna = False
        self.czestotliwosc = czestotliwosc  # Ton dźwięku w Hz
        self.czas_trwania = czas_trwania    # Czas trwania w ms

if __name__ == "__main__":
    gra1 = gra([])
    gra1.wczytaj_piosenke()

    try:
        gra1.uruchom()
    except KeyboardInterrupt:
        print("\nGra została przerwana. Do zobaczenia!")