import random

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
    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.tamanhetkinen_nopeus*aika)
        return self.kuljettu_matka


kisaAutot = []
for i in range(10):
    rekt = f"ABC-{i + 1}"
    huipn = random.randint(100,200)
    auto = Auto(rekt, huipn,0,0)
    list.append(kisaAutot,auto)
kisa = True
while kisa:
    #for auto in kisaAutot:
    for auto in kisaAutot:
        vauhti = random.randint(-10,15)
        auto.kiihdyta(vauhti)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            print(auto.kuljettu_matka)
            print(f"auto: {auto.rekisteritunnus} voitti kisan!!!")
            print("\nMuut kisaajat: ")
            kisaAutot.sort(key = lambda a: a.kuljettu_matka, reverse=True)
            for auto in kisaAutot:
                print("Auto: "+str(auto.rekisteritunnus) +"         Matka: "+str(auto.kuljettu_matka))
            kisa = False
            break
