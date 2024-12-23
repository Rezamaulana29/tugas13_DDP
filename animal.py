#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

#buat minimal 2 objek untuk setiap class childnya. 
class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print(f"\nNama\t\t\t: {self.name}")
        print(f"Makanan\t\t: {self.makanan}")
        print(f"Hidup\t\t\t: {self.hidup}")
        print(f"Berkembang Biak\t: {self.berkembang_biak}")
print("=====================================================")
class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sayap, kaki, warna_bulu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sayap = sayap
        self.kaki = kaki
        self.warna_bulu = warna_bulu

    def info_burung(self):
        self.info_animal()
        print(f"Sayap\t\t\t: {self.sayap}")
        print(f"Kaki\t\t\t: {self.kaki}")
        print(f"Warna Bulu\t\t: {self.warna_bulu}")
print("=====================================================")
class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sirip, insang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sirip = sirip
        self.insang = insang

    def info_ikan(self):
        self.info_animal()
        print(f"Sirip\t\t\t: {self.sirip}")
        print(f"Insang\t\t\t: {self.insang}")
print("=====================================================")
class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sisik, gigi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sisik = sisik
        self.gigi = gigi

    def info_ular(self):
        self.info_animal()
        print(f"Sisik\t\t\t: {self.sisik}")
        print(f"Gigi\t\t\t: {self.gigi}")
print("=====================================================")
#  objek class Animal
binatang = Animal("Kucing", "Daging", "17 tahun", "Melahirkan")
binatang.info_animal()

#  objek class Burung
burung1 = Burung("Elang", "Daging", "8 tahun", "Bertelur", "Panjang", "Kuat", "Coklat")
burung1.info_burung()

burung2 = Burung("Merpati", "Biji-bijian", "18 tahun", "Bertelur", "Pendek", "Lemah", "Abu-abu")
burung2.info_burung()

#  objek class Ikan 
ikan1 = Ikan("Ikan Hiu", "Daging", "35 tahun", "Bertelur", "Kuat", "Kuat")
ikan1.info_ikan()

ikan2 = Ikan("Ikan Guppy", "Plankton", "5 tahun", "Bertelur", "Lemah", "Lemah")
ikan2.info_ikan()

#  objek class Ular
ular1 = Ular("Ular sanca", "Daging", "25 tahun", "Bertelur", "Keras", "Tajam")
ular1.info_ular()

ular2 = Ular("Ular cobra", "Daging", "20 tahun", "Bertelur", "Keras", "Tajam")
ular2.info_ular()