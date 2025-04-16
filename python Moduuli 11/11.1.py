kumpi = True
class Julkaisu:
    def __init__(self,lehti,kirja):
        self.kirja = kirja
        self.lehti = lehti

    def tulosta_tiedot(self):
        if self.kirja is None:
            print(f"Lehti: {self.lehti}")
        if self.lehti is None:
            print(f"Kirja: {self.kirja}")


class Lehti(Julkaisu):
    def __init__(self,lehti,päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(lehti,None)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"   päätoimittaja: {self.päätoimittaja}")


class Kirja(Julkaisu):
    def __init__(self,kirja,kirjoittaja,sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(None,kirja)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"   kirjoittaja: {self.kirjoittaja}")
        print(f"   sivumäärä: {self.sivumäärä}")


kirjat = []
kirjat.append(Lehti("Aku Ankka","Aki Hyyppä"))
kirjat.append((Kirja("Hytti nor6 ", "Rosa likstrom", 200)))

for k in kirjat:
    k.tulosta_tiedot()