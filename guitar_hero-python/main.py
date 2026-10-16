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
            winsound.Beep(1000, 80)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

    def dzwiek(self, czestotliwosc, czas):
        def _graj():
            # Zabezpieczenie przed zbyt krótkim lub uciętym dźwiękiem
            winsound.Beep(int(czestotliwosc), max(int(czas), 50))
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

class gra:
    def __init__(self, nutki, tempo=180):
        self.nutki = nutki
        self.state = "start"
        self.dzwieki = MenedzerDzwiekowWinsound()
        self.screen = None
        self._aktualny_czas = 2.00  # Startowy czas pierwszej nuty
        self.tempo = tempo          # Ustawienie tempa (BPM)
        self.punkty = 0             # Licznik punktów gracza
        self.czcionka = None        # Inicjalizowana po uruchomieniu pygame

        # Dynamiczne przeliczanie wartości rytmicznych na podstawie aktualnego BPM
        krok_cwiercnuty = 60.0 / self.tempo
        
        self.RYTM = {
            "szesnastka": krok_cwiercnuty / 4.0,
            "osemka": krok_cwiercnuty / 2.0,
            "cwiercnuta": krok_cwiercnuty,
            "polnuta": krok_cwiercnuty * 2.0,
            "cala": krok_cwiercnuty * 4.0,
            "cwiercnuta_z_kropka": krok_cwiercnuty * 1.5,
            "osemka_z_kropka": krok_cwiercnuty * 0.75,
            "triole_cwiercnutowe": krok_cwiercnuty / 3.0,
        }

    def dodaj(self, kolumna, czestotliwosc, wartosc="osemka"):
        """Dodaje nutę o wybranej wartości rytmicznej i automatycznie przesuwa czas."""
        trwanie = self.RYTM.get(wartosc, self.RYTM["osemka"])
        czas_ms = int(trwanie * 1000)  
        
        self.nutki.append(nuta(
            kolumna=kolumna, 
            czas=self._aktualny_czas, 
            czestotliwosc=czestotliwosc, 
            czas_trwania=czas_ms, 
            dlugosc_trwania=trwanie
        ))
        self._aktualny_czas += trwanie
        
    def pauza(self, wartosc="osemka"):
        """Wstawia pauzę (przesuwa czas do przodu bez tworzenia nuty)."""
        trwanie = self.RYTM.get(wartosc, self.RYTM["osemka"])
        self._aktualny_czas += trwanie

    def wczytaj_piosenke(self):
        # Resetujemy licznik czasu na start (dajemy 2 sekundy buforu na ekranie)
        self._aktualny_czas = 2.00

        # Słownik częstotliwości (w Hz)
        E4 = 329.63
        G4 = 392.00
        A4 = 440.00
        Bb4 = 466.16
        B4 = 493.88
        C5 = 523.25
        D5 = 587.33
        Eb5 = 622.25
        E5 = 659.25
        F5 = 698.46
        Gb5 = 739.99
        G5 = 783.99
        A5 = 880.00
        B5 = 987.77
        Ab4 = 415.30
        C4 = 261.63

        # --- Takt 1 & 2 (G) ---
        self._aktualny_czas = 2.00
        self.dodaj(2, E5, "osemka")
        self.dodaj(2, E5, "osemka")
        self.pauza("osemka")
        self.dodaj(2, E5, "osemka")
        self.pauza("osemka")
        self.dodaj(1, C5, "osemka")
        self.dodaj(2, E5, "cwiercnuta")
        
        self.dodaj(4, G5, "cwiercnuta")
        self.pauza("cwiercnuta")
        self.dodaj(3, G4, "cwiercnuta")
        self.pauza("cwiercnuta")
        
        # --- Takt 3 & 4 (C) ---
        for _ in range(2):
            self.dodaj(1, C5, "cwiercnuta")
            self.pauza("osemka")
            self.dodaj(3, G4, "cwiercnuta")
            self.pauza("osemka")
            self.dodaj(2, E4, "cwiercnuta")
            
            self.pauza("osemka")
            self.dodaj(3, A4, "cwiercnuta")
            self.dodaj(4, B4, "cwiercnuta")
            self.dodaj(3, Bb4, "osemka")
            self.dodaj(2, A4, "cwiercnuta")

            # --- Takt 5 & 6 (Triole i domknięcie) ---
            self.dodaj(1, G4, "triole_cwiercnutowe")
            self.dodaj(2, D5, "triole_cwiercnutowe")
            self.dodaj(3, G5, "triole_cwiercnutowe")
            self.dodaj(4, A5, "cwiercnuta")
            self.dodaj(3, F5, "osemka")
            self.dodaj(2, G5, "osemka")

            self.pauza("osemka")
            self.dodaj(1, E5, "cwiercnuta")
            self.dodaj(2, C5, "osemka")
            self.dodaj(3, D5, "osemka")
            self.dodaj(4, B4, "cwiercnuta")
            self.pauza("osemka")

        # --- Takty 7-10 (Przejście z chromatyką) ---
        for _ in range(2):
            self.pauza("cwiercnuta")
            self.dodaj(4, G5, "osemka")
            self.dodaj(3, Gb5, "osemka")
            self.dodaj(2, F5, "osemka")
            self.dodaj(1, Eb5, "cwiercnuta")
            self.dodaj(2, E5, "osemka")

            # Takt 8 (F)
            self.pauza("osemka")
            self.dodaj(2, Ab4, "osemka")
            self.dodaj(3, A4, "osemka")
            self.dodaj(4, C5, "osemka")
            self.pauza("osemka")
            self.dodaj(1, A4, "osemka")
            self.dodaj(1, C5, "osemka")
            self.dodaj(1, D5, "osemka")

            # Takt 9 (C)
            self.pauza("cwiercnuta")
            self.dodaj(2, G5, "osemka")
            self.dodaj(3, Gb5, "osemka")
            self.dodaj(2, F5, "osemka")
            self.dodaj(1, Eb5, "cwiercnuta")
            self.dodaj(4, E5, "osemka")

            # Takt 10 (G)
            self.pauza("osemka")
            self.dodaj(4, B5, "cwiercnuta")
            self.dodaj(4, B5, "osemka")
            self.dodaj(4, B5, "cwiercnuta")
            self.pauza("cwiercnuta")

            self.pauza("cwiercnuta")
            self.dodaj(4, G5, "osemka")
            self.dodaj(3, Gb5, "osemka")
            self.dodaj(2, F5, "osemka")
            self.dodaj(1, Eb5, "cwiercnuta")
            self.dodaj(2, E5, "osemka")
            
            # Takt 12 (F)
            self.pauza("osemka")
            self.dodaj(2, Ab4, "osemka")
            self.dodaj(3, A4, "osemka")
            self.dodaj(4, C5, "osemka")
            self.pauza("osemka")
            self.dodaj(1, A4, "osemka")
            self.dodaj(1, C5, "osemka")
            self.dodaj(1, D5, "osemka")

            self.pauza("cwiercnuta")
            self.dodaj(2, Eb5, "cwiercnuta")
            self.pauza("osemka")
            self.dodaj(3, D5, "cwiercnuta")
            self.pauza("osemka")

            self.dodaj(4, C5, "cwiercnuta")
            self.pauza("cwiercnuta")
            self.pauza("polnuta")

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
            
            if -1.0 <= czas_do_uderzenia <= 2.5:
                y_pozycja = y_uderzenia - (czas_do_uderzenia * skala_y)
                wysokosc_nuty = n.dlugosc_trwania * skala_y
                y_pozycja_prostokata = y_pozycja - wysokosc_nuty
                x_pozycja = (n.kolumna - 1) * szerokosc_kolumny + (szerokosc_kolumny // 2) - 15
                
                kolor_nuty = ZOLTY if n.trafiona else ZIELONY
                pygame.draw.rect(self.screen, kolor_nuty, (x_pozycja, y_pozycja_prostokata, 30, max(int(wysokosc_nuty), 10)))

        # Wyświetlanie punktów na ekranie
        tekst_punktow = self.czcionka.render(f"Punkty: {self.punkty}", True, BIALY)
        self.screen.blit(tekst_punktow, (10, 10))

        pygame.display.flip()

    def sprawdz_wejscie(self, kolumna):
        aktualny_czas = pygame.time.get_ticks() / 1000.0
        okno_trafienia = 0.15  # tolerancja w sekundach (ok. 150 ms)

        for n in self.nutki:
            if n.kolumna == kolumna and not n.trafiona:
                roznica = abs(n.czas - aktualny_czas)
                
                if roznica <= okno_trafienia:
                    n.trafiona = True
                    self.punkty += 100  # Dodajemy 100 punktów za trafienie
                    print("Trafienie! (Hit) +100 pkt")
                    self.dzwieki.dzwiek(n.czestotliwosc, n.czas_trwania)
                    return

        print("Pudło! -50 pkt")
        self.punkty = max(0, self.punkty - 50)  # Opcjonalnie: kara za pudło (nie schodzimy poniżej 0)
        self.dzwieki.odtworz_pudlo()

    def uruchom(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        self.czcionka = pygame.font.SysFont("Arial", 24)  # Inicjalizacja czcionki
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
    def __init__(self, kolumna, czas, czestotliwosc=440, czas_trwania=150, dlugosc_trwania=0.15):
        self.kolumna = kolumna
        self.czas = czas
        self.trafiona = False
        self.aktywna = False
        self.czestotliwosc = czestotliwosc
        self.czas_trwania = czas_trwania        
        self.dlugosc_trwania = dlugosc_trwania  

if __name__ == "__main__":
    gra1 = gra([], tempo=100)
    gra1.wczytaj_piosenke()

    try:
        gra1.uruchom()
    except KeyboardInterrupt:
        print("\nGra została przerwana. Do zobaczenia!")