class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        tamanhetkinen_nopeus = 0
        kuljettu_matka = 0

    def kiihdyta(self, muutos):
        auto.tamanhetkinen_nopeus = auto.tamanhetkinen_nopeus + muutos
        if self.tamanhetkinen_nopeus <0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus > int(self.huippunopeus):
            self.tamanhetkinen_nopeus = int(self.huippunopeus)
        return self.tamanhetkinen_nopeus
    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.tamanhetkinen_nopeus*aika)
        return self.kuljettu_matka


auto = Auto("ABC,123", 142,60,2000)

auto.kulje(1.5)
print(auto.rekisteritunnus)
print(str(auto.huippunopeus) + " km/h")
print(auto.kuljettu_matka)
print(auto.tamanhetkinen_nopeus)