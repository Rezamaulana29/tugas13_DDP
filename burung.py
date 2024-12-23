#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method
 
#buat minimal 2 objek untuk setiap class childnya.

from animal import Animal

class Burung(Animal):
    def _init_(self,nama,makanan,hidup,berkembang_biak,paruh,warna_bulu):
        super ()._init_(nama,makanan,hidup,berkembang_biak),
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super ().info_animal(),
        print("paruh\t\t\t :", self.paruh,
             "\nwarna_bulu\t\t :", self.warna_bulu,)

burung_beo = Burung("beo","jagung","5 tahun","bertelur","melengkung","warna warni")
burung_beo.info_burung()
print("=============================================")
burung_merpati = Burung ("Merpati","beras","5 tahun","bertelur","melengkung","putih")
burung_merpati.info_burung()