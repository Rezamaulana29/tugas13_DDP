from animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sisik, gigi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sisik = sisik
        self.gigi = gigi

    def info_ular(self):
        self.info_animal()
        print(f"Sisik\t\t\t: {self.sisik}")
        print(f"Gigi\t\t\t: {self.gigi}")