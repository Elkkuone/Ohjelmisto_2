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


#pitää selvittää miksi tämä ei toiminut
"""        while haluttuKerros != self.nykykerros:
            print(f"siirrytään {haluttuKerros} kerrokseen")
            print(self.nykykerros)
            print(haluttuKerros)
            if nykyinenKerros > haluttuKerros:
                self.kerrosAlas()
            elif haluttuKerros < nykyinenKerros:
                self.kerrosYlos()
            elif haluttuKerros == nykyinenKerros:
                print(f"saavuimme {haluttuKerros} !")
            else:
                print("jotain meni vituiksi")
                break"""


#hissin yläraja ja alaraja
h = Hissi(0,5)
h.siirryKerrokseen(5)
h.siirryKerrokseen(0)