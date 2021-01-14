import sqlite3

class Kisiler:
    def __init__(self):
        self.connect = sqlite3.connect("kisiler.db")
        self.cursor = self.connect.cursor()
        self.verileriOku()
        print("Veritabanındaki vatandaş sayısı:", len(self.verileriOku()))

    def verileriOku(self):
        self.cursor.execute("SELECT * FROM kisiler")
        kisiler = self.cursor.fetchall()
        return kisiler
    def dbGuncelle(self):
        self.connect.commit()
    def tablo_olustur(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kisiler (kimlikNo INT, Adı TEXT, SoyAdı TEXT,BabaAdı TEXT,AnneAdı TEXT,DoğumYeri TEXT,MedeniDurumu TEXT,"
                            "KanGrubu TEXT,KütükŞehir TEXT,Kütükİlçe TEXT,İkametgahŞehir TEXT,İkametgahİlçe TEXT)")
        self.dbGuncelle()
    def kisi_olustur(self):
        self.kimlikNo = self.kimlikNoGirme()
        for i in self.verileriOku():
            if i[0] == self.kimlikNo:
                print("{} kimlik numaralı kişi kayıtlıdır.".format(self.kimlikNo))
                self.cikis()
        self.adi = input("Veritabanına girilecek olan kişinin adını giriniz: ").lower().capitalize()
        self.soyadi = input("Veritabanına girilecek olan kişinin soyadını giriniz: ").lower().capitalize()
        self.babaAdi= input("Veritabanına girilecek olan kişinin baba adını giriniz: ").lower().capitalize()
        self.anneAdi = input("Veritabanına girilecek olan kişinin anne adını giriniz: ").lower().capitalize()
        self.dogumYeri = input("Veritabanına girilecek olan kişinin doğum yerini giriniz: ").lower().capitalize()
        self.medeniDurumu = input("Veritabanına girilecek olan kişinin medeni durumu: ").lower().capitalize()
        self.kanGrubu = input("Veritabanına girilecek olan kişinin kan grubunu giriniz: ").lower().capitalize()
        self.kutukSehir = input("Veritabanına girilecek olan kişinin kütük şehrini giriniz: ").lower().capitalize()
        self.kutukIlce= input("Veritabanına girilecek olan kişinin kütük ilçesini giriniz: ").lower().capitalize()
        self.ikametgahSehir = input("Veritabanına girilecek olan kişinin ikametgah şehrini giriniz.").lower().capitalize()
        self.ikametgahIlce = input("Veritabanına girilecek olan kişinin ikametgah ilçesini giriniz: ").lower().capitalize()
        self.cursor.execute("INSERT INTO kisiler VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
        (self.kimlikNo, self.adi, self.soyadi, self.babaAdi, self.anneAdi, self.dogumYeri, self.medeniDurumu, self.kanGrubu,
        self.kutukSehir, self.kutukIlce,self.ikametgahSehir, self.ikametgahIlce))
        self.dbGuncelle()
        print("Vatandaş veritabanına eklendi.")
    def kisi_silme(self):
        self.kimlikNo = self.kimlikNoGirme()
        for i in self.verileriOku():
            if i[0] == self.kimlikNo:
                self.cursor.execute("Delete from kisiler where kimlikNo= ?",(self.kimlikNo,))
                self.dbGuncelle()
                print("Vatandaş veritabanından silindi.")
                break
        else:
            print("Kişi bulunamadı")
    def bilgiGuncelle(self):
        self.kimlikNo = self.kimlikNoGirme()
        for i in self.verileriOku():
            if i[0] == self.kimlikNo:
                operations = ["kimlikNo","Adı","SoyAdı","BabaAdı","AnneAdı","DoğumYeri","MedeniDurumu","KanGrubu","KütükŞehir" ,"Kütükİlçe","İkametgahŞehir" ,"İkametgahİlçe"]
                while True:
                    try:
                        updateSelect = int(input("1-)Kimlik No\n2-)Adı\n3-)Soyadı\n4-)Baba Adı\n5-)Anne Adı\n6-)Doğum Yeri\n7-)Medeni Durumu\n"
                                                 "8-)Kan Grubu\n9-)Kütük Şehir\n10-)Kütük İlçe\n11-)İkametgah Şehir\n12-)İkametgah İlçe\nSeçiniz: "))
                        if int(updateSelect) < 1 or int(updateSelect) > 12:
                            print("Lütfen 1 ile 12 arasında bir sayı giriniz.")
                            continue
                        break
                    except ValueError:
                        print("Yanlış giriş!! Lütfen tam sayı bir değer giriniz.")
                yeniDeger = input("{} için yeni değeri giriniz: ".format(operations[updateSelect-1])).lower().capitalize()
                self.cursor.execute("UPDATE kisiler SET {} = '{}' WHERE kimlikNo='{}'".format(operations[updateSelect - 1], yeniDeger,self.kimlikNo))
                self.dbGuncelle()
                print("{} kimlik nolu vatandaşın bilgileri güncellendi.".format(self.kimlikNo,))
                break
        else:
            print("Kişi bulunamadı")
    def veri_listele(self):
        print("Vatandas Listesi Hazırlanıyor ...")
        for i in self.verileriOku():
            print(i)
    def arastir(self):
        self.kimlikNo = self.kimlikNoGirme()
        for i in self.verileriOku():
            if int(i[0]) == int(self.kimlikNo):
                print(i)
                break
        else:
            print("Kişi bulunamadı")
    def kimlikNoGirme(self):
        while True:
            try:
                self.kimlikNo = int(input("Veritabanında işlem yapılacak kişinin kimlik numarasını giriniz: "))
                break
            except ValueError:
                print("Lütfen tam sayı bir değer giriniz. Doğru tip: int")
        return self.kimlikNo


    def cikis(self):
        self.connect.close()
        exit(0)
