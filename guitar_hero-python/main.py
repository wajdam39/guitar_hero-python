
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
            # Częstotliwość 1000 Hz, czas trwania 80 ms (krótki, nierysujący zwiechy)
            winsound.Beep(400, 80)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()
    def dzwiek(self, czestotliwosc, czas):
            """Odtwarza krótki, ostrzegawczy dźwięk pudła w osobnym wątku."""
        def _graj():
            # Częstotliwość 1000 Hz, czas trwania 80 ms (krótki, nierysujący zwiechy)
            winsound.Beep(czestotliwosc, czas)
        watek = threading.Thread(target=_graj)
        watek.daemon = True
        watek.start()

class gra:
  # Konstruktor (inicjalizacja obiektu)
    def __init__(self,nutki):
        self.nutki = nutki
        self.state = "start"
        self.dzwieki = MenedzerDzwiekowWinsound()
        self.screen = None  # Inicjalizacja atrybutu screen na None

    def wczytaj_piosenke(self): # tworzy i zapełnia listę self.nutki przykładowymi nutami o konkretnych czasach.
        self.nutki.append(nuta(kolumna=1, czas=2.0))  # Nuta w 1. kolumnie za 2 sekundy
        self.nutki.append(nuta(kolumna=2, czas=2.5))  # Nuta w 2. kolumnie za 2.5 sekundy
        self.nutki.append(nuta(kolumna=3, czas=3.0))  # Nuta w 3. kolumnie za 3 sekundy
        self.nutki.append(nuta(kolumna=4, czas=3.5))  # Nuta w 4. kolumnie za 3.5 sekund
        self.nutki.append(nuta(kolumna=2, czas=4.5))  # Kolejna nuta w 2. kolumnie za 4.5 sekundy
        self.nutki.append(nuta(kolumna=1, czas=5.0))  # I tak dalej...
    
    def rysuj_planszę(self):# odpowiada za czyszczenie terminala i wyświetlanie kolumn oraz nut, które aktualnie spadają.
       self.screen.fill((0, 0, 0))
       BIALY = (255, 255, 255)
       ZIELONY = (0, 255, 0)
       CZERWONY = (255, 0, 0)
       ZOLTY = (255, 255, 0)
       szerokosc_kolumny = 100
       
       for i in range(1, 4):
            x = i * szerokosc_kolumny
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, 600), 2)

       y_uderzenia = 500
       pygame.draw.line(self.screen, BIALY, (0, y_uderzenia), (400, y_uderzenia), 4)

       aktualny_czas = pygame.time.get_ticks() / 1000.0
       for nuta in self.nutki:
            # Obliczamy pozycję Y na podstawie czasu
            # Załóżmy, że nuta spada przez 2 sekundy zanim dotrze do linii uderzenia
            czas_do_uderzenia = nuta.czas - aktualny_czas
            
            # Jeśli nuta jest w naszym "oknie widoczności" (np. 2 sekundy przed uderzeniem)
            if -0.5 <= czas_do_uderzenia <= 2.0:
                # Przeliczamy czas na piksele (im mniejszy czas_do_uderzenia, tym bliżej y_uderzenia)
                # 2 sekundy = 500 pikseli drogi
                y_pozycja = y_uderzenia - (czas_do_uderzenia * (y_uderzenia / 2.0))
                # Wyznaczamy środek kolumny (kolumny: 1, 2, 3, 4)
                x_pozycja = (nuta.kolumna - 1) * szerokosc_kolumny + (szerokosc_kolumny // 2) - 15
                if nuta.trafiona:
                    kolor_nuty = ZOLTY
                else:
                    kolor_nuty = ZIELONY
                # Rysujemy nutę jako prostokąt
                pygame.draw.rect(self.screen, kolor_nuty, (x_pozycja, y_pozycja, 30, 15))

       pygame.display.flip()

    def sprawdz_wejscie(self, kolumna,czestotliwosc,czas): # sprawdza, czy gracz wcisnął odpowiedni klawisze i czy nuta była w tym momencie blisko linii uderzenia.
        aktualny_czas = pygame.time.get_ticks() / 1000.0
        okno_trafienia = 0.15  # tolerancja w sekundach (ok. 150 ms)

        trafiono_cokolwiek = False
        
        for nuta in self.nutki:
            # Sprawdzamy tylko nietrafione nuty w wybranej kolumnie
            if nuta.kolumna == kolumna and not nuta.trafiona:
                roznica = abs(nuta.czas - aktualny_czas)
                
                if roznica <= okno_trafienia:
                    nuta.trafiona = True
                    print("Trafienie! (Hit)")
                    self.dzwieki.dzwiek(czestotliwosc, czas)
                    return
                else:
                    print("Pudło!")
                    self.dzwieki.odtworz_pudlo()
                    return
            print("Pudło!)")
            self.dzwieki.odtworz_pudlo()

               
    def uruchom(self): # główna pętla gry (while), która kręci się co klatkę (np. co 0.03 sekundy), aktualizuje czas i odświeża ekran.       while True:
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # obsługa zamknięcia okna
                    return
                elif event.type == pygame.KEYDOWN:
                    # obsługa wciśnięcia klawisza przez gracza
                    if event.key == pygame.K_1:
                        self.sprawdz_wejscie(1)
                    elif event.key == pygame.K_2:
                        self.sprawdz_wejscie(2)
                    elif event.key == pygame.K_3:
                        self.sprawdz_wejscie(3)
                    elif event.key == pygame.K_4:
                        self.sprawdz_wejscie(4)
            pygame.time.get_ticks() / 1000.0
            self.rysuj_planszę()

    

class nuta:
  # Konstruktor (inicjalizacja obiektu)
  def __init__(self,kolumna,czas,czestotliwosc=440, czas_trwania=200):
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
        # Obsługa, gdy gracz wciśnie Ctrl+C, żeby wyjść z gry
        print("\nGra została przerwana. Do zobaczenia!")