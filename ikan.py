from animal import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sirip, insang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sirip = sirip
        self.insang = insang

    def info_ikan(self):
        self.info_animal()
        print(f"Sirip\t\t\t: {self.sirip}")
        print(f"Insang\t\t\t: {self.insang}")