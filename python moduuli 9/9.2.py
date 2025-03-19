class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        tamanhetkinen_nopeus = 0
        kuljettu_matka = 0




print("kerro auton nopeus: ")
nopeus = input()
def kiihdyta(nopeus,autonopeus):

auto = Auto("ABC,123", "142 km/h", 0, 0)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.kuljettu_matka)
print(auto.tamanhetkinen_nopeus)