class Työntekijä:
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.etunimi} {self.sukunimi}")


class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in työntekijät:
    t.tulosta_tiedot()
