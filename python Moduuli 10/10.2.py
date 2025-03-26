class Hissi:
    def __init__ (self, alin, ylin):
        self.ylin = ylin
        self.alin = alin
        self.nykykerros = alin
    def kerrosYlos(self):
        self.nykykerros = self.nykykerros+1
        print(f"olemme {self.nykykerros} kerroksessa")
    def kerrosAlas(self):
        self.nykykerros = self.nykykerros -1
        print(f"olemme {self.nykykerros} kerroksessa")

    def siirryKerrokseen(self, haluttuKerros):
        while haluttuKerros > self.nykykerros:
            self.kerrosYlos()
        while haluttuKerros <self.nykykerros:
            self.kerrosAlas()
        print(f"saavuimme {haluttuKerros} kerrokseen")
class Talo:
    Hissit = []
    def __init__(self, alin, ylin, maara):
        self.hissiLista = [Hissi(alin, ylin)for i in range(maara)]
    def liikkuu(self,hisnro,kerros):
        self.hissiLista[hisnro].siirryKerrokseen(kerros)
        print(f"Hissi {hisnro} on kerroksessa {kerros}")



talo = Talo(0,5,5)

talo.liikkuu(1,7)
talo.liikkuu(0,4)
talo.liikkuu(2,100)
talo.liikkuu(3,5)
talo.liikkuu(4,69420)

