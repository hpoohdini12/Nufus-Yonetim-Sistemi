from proje import Kisiler
class anaEkran(Kisiler):
    def __init__(self):
        super().__init__()
    def menu(self):

        print("VATANDAŞ VERITABANI".center(100, "*").upper())
        print("1-) Vatandaş ekleme\n"
              "2-) Vatandaş silme\n"
              "3-) Vatandaş bilgi güncelleme\n"
              "4-) Vatandaş listeleme\n"
              "5-) Vatandaş arama\n"
              "6-) Çıkış\n")
        while True:
            try:
                choice = int(input("Your choice: "))
                if int(choice) < 1 or int(choice) > 6:
                    print("Lütfen 1-6 arası bir sayı giriniz.")
                    continue
                break
            except ValueError:
                print("Yanlış giriş!! Lütfen tam sayı bir değer giriniz.")
        return choice

    def calistir(self):
        choice = self.menu()
        if choice == 1:
            self.kisi_olustur()
        if choice == 2:
            self.kisi_silme()
        if choice == 3:
            self.bilgiGuncelle()
        if choice == 4:
            self.veri_listele()
        if choice == 5:
            self.arastir()
        if choice == 6:
            self.cikis()


calistir = anaEkran()
while True:
    calistir.calistir()
