import pygame
import os
import time
import winsound
import threading
import utwory

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
        self.tempo = tempo          # Ustawienie tempo (BPM)
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
            "triole_cwiercnutowe": (krok_cwiercnuty * 2.0) / 3.0,
            "polnuta_z_kropka": krok_cwiercnuty * 3.0,
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

        # Wyświetlanie punktów oraz aktualnego tempa na ekranie
        tekst_punktow = self.czcionka.render(f"Punkty: {self.punkty} | BPM: {self.tempo}", True, BIALY)
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
                    
                    # Liczenie punktów uwzględniające tempo (im wyższe BPM, tym większa premia)
                    mnozniki_tempo = self.tempo / 100.0
                    przyrost_punktow = int(100 * mnozniki_tempo)
                    
                    self.punkty += przyrost_punktow
                    print(f"Trafienie! (Hit) +{przyrost_punktow} pkt")
                    self.dzwieki.dzwiek(n.czestotliwosc, n.czas_trwania)
                    return

        kara = int(50 * (self.tempo / 100.0))
        print(f"Pudło! -{kara} pkt")
        self.punkty = max(0, self.punkty - kara)  # Nie schodzimy poniżej 0 punktów
        self.dzwieki.odtworz_pudlo()

    def uruchom(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        self.czcionka = pygame.font.SysFont("Arial", 22)  # Inicjalizacja czcionki
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
    # Możesz zmienić tempo tutaj, np. 180
    gra1 = gra([], tempo=150)
    utwory.wczytaj_Thank_You_Not_So_Bad(gra1)  # tempo: 150 BPM
    gra2 = gra([], tempo=180)
    utwory.wczytaj_mario(gra2)  # tempo: 180 BPM

    try:
        gra1.uruchom()
    except KeyboardInterrupt:
        print("\nGra została przerwana. Do zobaczenia!")