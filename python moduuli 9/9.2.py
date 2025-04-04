class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        tamanhetkinen_nopeus = 0
        kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + muutos
        if self.tamanhetkinen_nopeus <0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus > int(self.huippunopeus):
            self.tamanhetkinen_nopeus = int(self.huippunopeus)
        return self.tamanhetkinen_nopeus


auto = Auto("ABC,123", 142,0,0)

muutos = 30
auto.kiihdyta(muutos)
muutos = 70
Auto.kiihdyta(auto,muutos)

muutos = 50
auto.kiihdyta(muutos)
print(auto.tamanhetkinen_nopeus)

muutos = -200
auto.kiihdyta(muutos)
print(auto.tamanhetkinen_nopeus)


auto.kiihdyta(muutos)
print(auto.rekisteritunnus)
print(str(auto.huippunopeus) + " km/h")
print(auto.kuljettu_matka)
print(auto.tamanhetkinen_nopeus)