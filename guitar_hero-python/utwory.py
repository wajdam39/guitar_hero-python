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
Db5 = 554.37
Ab5 = 830.61
Bb5 = 932.33
C6 = 1046.50


def wczytaj_mario(self):
        # Resetujemy licznik czasu na start (dajemy 2 sekundy buforu na ekranie)
        self._aktualny_czas = 2.00

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
            self.dodaj(4, E5, "cwiercnuta")
            self.dodaj(2, C5, "osemka")
            self.dodaj(3, D5, "osemka")
            self.dodaj(1, B4, "cwiercnuta")
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
            self.dodaj(4, C6, "cwiercnuta")
            self.dodaj(4, C6, "osemka")
            self.dodaj(4, C6, "cwiercnuta")
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

        self.dodaj(3, C5, "osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.dodaj(4, D5, "cwiercnuta")

        self.dodaj(4, E5, "osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(2, A4, "osemka")
        self.dodaj(1, G4, "polnuta")

        self.dodaj(3, C5, "osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.dodaj(4, D5, "osemka")
        self.dodaj(4, E5, "osemka")

        self.pauza("cala")

        self.dodaj(3, C5, "osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, C5, "osemka")
        self.dodaj(4, D5, "cwiercnuta")

        self.dodaj(4, E5, "osemka")
        self.dodaj(3, C5, "osemka")
        self.pauza("osemka")
        self.dodaj(2, A4, "osemka")
        self.dodaj(1, G4, "polnuta")

        self.dodaj(3, E5, "osemka")
        self.dodaj(3, E5, "osemka")
        self.pauza("osemka")
        self.dodaj(3, E5, "osemka")
        self.pauza("osemka")
        self.dodaj(2, C5, "osemka")
        self.dodaj(3, E5, "cwiercnuta")

        self.dodaj(4, G5, "cwiercnuta")
        self.pauza("cwiercnuta")
        self.dodaj(3, G4, "cwiercnuta")
        self.pauza("cwiercnuta")

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

            self.dodaj(1, G4, "triole_cwiercnutowe")
            self.dodaj(2, D5, "triole_cwiercnutowe")
            self.dodaj(3, G5, "triole_cwiercnutowe")
            self.dodaj(4, A5, "cwiercnuta")
            self.dodaj(3, F5, "osemka")
            self.dodaj(4, G5, "osemka")

            self.pauza("osemka")
            self.dodaj(4, E5, "cwiercnuta")
            self.dodaj(2, C5, "osemka")
            self.dodaj(3, D5, "osemka")
            self.dodaj(1, B4, "cwiercnuta")
            self.pauza("osemka")

def wczytaj_Thank_You_Not_So_Bad(self):
        # Resetujemy licznik czasu na start (dajemy 2 sekundy buforu na ekranie)
        self._aktualny_czas = 2.00

        self.pauza("cwiercnuta")
        self.pauza("osemka")
        self.dodaj(1, Bb4, "osemka")
        self.dodaj(3, F5, "cwiercnuta")
        self.dodaj(3, F5, "cwiercnuta")

        self.dodaj(3, F5, "cwiercnuta")
        self.dodaj(4, Gb5, "osemka")
        self.dodaj(2, Eb5, "cwiercnuta")
        self.dodaj(1, Db5, "cwiercnuta")
        self.dodaj(3, F5, "osemka")

        self.dodaj(1, Db5, "osemka")
        self.dodaj(2, Eb5, "polnuta")
        self.pauza("cwiercnuta")
        self.dodaj(1, C5, "osemka")
        #takt 4
        self.dodaj(2, Db5, "cwiercnuta")
        self.dodaj(4, F5, "cwiercnuta")
        self.dodaj(2, C5, "cwiercnuta")
        self.dodaj(4, F5, "osemka")
        self.dodaj(1, Bb4, "cwiercnuta")

        self.pauza("cwiercnuta")
        self.dodaj(1, Bb4, "osemka")
        self.dodaj(3, F5, "osemka")
        self.dodaj(3, F5, "cwiercnuta")
        self.dodaj(3, F5, "cwiercnuta")

        self.dodaj(4, Gb5, "cwiercnuta")
        self.dodaj(2, Eb5, "cwiercnuta")
        self.dodaj(1, Db5, "cwiercnuta")
        self.dodaj(3, F5, "cwiercnuta")
        
        self.dodaj(1, Eb5, "polnuta")
        self.pauza("cwiercnuta")
        self.dodaj(1, C5, "osemka")
        #takt 8
        self.dodaj(3, Ab5, "cwiercnuta")
        self.dodaj(4, Bb5, "cwiercnuta")
        self.dodaj(2, F5, "cwiercnuta")
        self.dodaj(1, Eb5, "osemka")
        self.dodaj(3, F5, "cwiercnuta")

        self.pauza("osemka")
        self.dodaj(1, Db5, "osemka")
        self.dodaj(2, Gb5, "osemka")
        self.dodaj(2, Gb5, "cwiercnuta")
        self.dodaj(2, Gb5, "cwiercnuta")

        self.dodaj(4, Bb5, "cwiercnuta")
        self.dodaj(2, Eb5, "cwiercnuta")
        self.dodaj(2, Eb5, "osemka")
        self.dodaj(1, Db5, "osemka")
        self.dodaj(3, F5, "cwiercnuta")

        self.dodaj(1, Db5, "cwiercnuta")
        self.dodaj(2, Eb5, "cwiercnuta_z_kropka")
        self.dodaj(1, Db5, "osemka")
        self.dodaj(2, Eb5, "osemka")

        self.dodaj(3, F5, "cwiercnuta")
        self.dodaj(4, Gb5, "osemka")
        self.dodaj(3, F5, "cwiercnuta")
        self.dodaj(3, F5, "osemka")
        self.dodaj(2, Eb5, "osemka")
        self.dodaj(1, F5, "cwiercnuta_z_kropka")
        self.pauza("cwiercnuta")

        self.dodaj(1, Bb5, "cwiercnuta")
        self.dodaj(4, F5, "osemka")
        self.dodaj(3, Eb5, "cwiercnuta_z_kropka")

        self.pauza("osemka")
        self.dodaj(2, Db5, "cwiercnuta_z_kropka")
        self.dodaj(1, Bb4, "osemka")
        self.dodaj(3, Db5, "osemka")

        self.dodaj(4, F5, "cwiercnuta")
        self.dodaj(2, Db5, "cwiercnuta")
        self.dodaj(3, Eb5, "osemka")
        self.dodaj(2, Db5, "osemka")
        self.dodaj(1, Bb4, "cwiercnuta_z_kropka")
        self.pauza("osemka")
