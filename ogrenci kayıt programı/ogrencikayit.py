class Ogrenci:
    def __init__(self, isim, yas, notu):
        self.isim = isim
        self.yas = yas
        self.notu = notu

    def __str__(self):
        return f'İsim: {self.isim}, Yaş: {self.yas}, Not: {self.notu}'

class OgrenciYonetici:
    def __init__(self):
        self.ogrenci_listesi = []

    def ogrenci_ekle(self, ogrenci):
        self.ogrenci_listesi.append(ogrenci)

    def ogrencileri_goruntule(self):
        for ogrenci in self.ogrenci_listesi:
            print(ogrenci)

    def dosyaya_kaydet(self, dosya_adi):
        try:
            with open(dosya_adi, 'w', encoding = "utf-8") as dosya:
                for ogrenci in self.ogrenci_listesi:
                    dosya.write(f'{ogrenci.isim},{ogrenci.yas},{ogrenci.notu}\n')
        except Exception as hata:
            print(f'Hata: {hata}')

    def dosyadan_yukle(self, dosya_adi):
        try:
            with open(dosya_adi, 'r', encoding = "utf-8") as dosya:
                self.ogrenci_listesi = []
                for satir in dosya:
                    isim, yas, notu = satir.strip().split(',')
                    self.ogrenci_listesi.append(Ogrenci(isim, int(yas), int(notu)))
        except Exception as hata:
            print(f'Hata: {hata}')

def kullanici_menu():
    yonetici = OgrenciYonetici()
    while True:
        print("------------------------------------------------------------------")
        print("\t\tÖğrenci Dosya Yönetim Sistemi Menüsü")
        print("------------------------------------------------------------------")
        print("\t\t\t<< Seçenekler >>")
        print("------------------------------------------------------------------")
        print("\t\t<1> Yeni bir öğrenci ekleyin ")
        print("\t\t<2> Öğrencileri görüntüleyin ")
        print("\t\t<3> Öğrencileri bir dosyaya kaydedin ")
        print("\t\t<4> Öğrencileri bir dosyadan yükleyin ")
        print("\t\t<5> Çıkış")
        secim = input("\t\tSeçiminizi yapın (sayı girin): ")
        if secim == '1':
            isim = input("Öğrencinin ismini girin: ").capitalize()
            while True:
                try:
                    yas = int(input("Öğrencinin yaşını girin: "))
                    break
                except ValueError:
                    print("Lütfen bir sayı girin!")
            while True:
                try:
                    notu = int(input("Öğrencinin notunu girin: "))
                    if(notu < 0 or notu > 100):
                        print("Lütfen 0-100 arası bir sayı girin!")
                        continue
                    break
                except ValueError:
                    print("Lütfen bir sayı girin!")
            yonetici.ogrenci_ekle(Ogrenci(isim, yas, notu))
        elif secim == '2':
            yonetici.ogrencileri_goruntule()
        elif secim == '3':
            dosya_adi = input("Dosya adını girin: ")
            yonetici.dosyaya_kaydet(dosya_adi)
        elif secim == '4':
            dosya_adi = input("Dosya adını girin: ")
            yonetici.dosyadan_yukle(dosya_adi)
        elif secim == '5':
            break

if __name__ == "__main__":
    kullanici_menu()