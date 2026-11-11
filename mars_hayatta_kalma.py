kimlik_no = input("Kimlik kodunuzu giriniz (Örnek: MARS-MÜH-99): ").upper().split("-")

if len(kimlik_no) != 3:
    print("Hatalı giriş.")
    exit()

if kimlik_no[2] != "99":
    print("Yüzeye çıkma izniniz yok.")
    exit()

dep = input("Departmanınızı giriniz (Örnek: tip, mühendislik, güvenlik): ").lower()

if dep not in ["tip", "mühendislik", "biyokimya", "güvenlik"]:
    print("Hatalı giriş.")
    exit()
else:
    print("Doğrulamam tamam.")

radyasyon = float(input("Radyasyon seviyenizi giriniz: "))

if radyasyon < 0 or radyasyon > 100:
    print("Hatalı giriş yaptınız veya radyasyon çok fazla.")
    exit()

if radyasyon > 75 and dep != "tip":
    print("Sadece tıpçılar bu seviyede giriş yapabilir.")
    exit()
elif radyasyon > 75 and dep == "tip":
    print("Giriş yapabilirsiniz.")

balance = 5000

suit = input("Giymek istediğiniz suiti seçiniz: (Hafif-1000 / Zirhli-2500 / Meka-4500): ").lower()

if suit not in ["hafif", "zirhli", "meka"]:
    print("Hatalı giriş.")
    exit()

if suit == "hafif":
    balance -= 1000
elif suit == "zirhli":
    balance -= 2500
elif suit == "meka":
    balance -= 4500

if dep == "tip" and suit == "meka":
    print("Tıpçılar meka giyemez! Hafif zırh verildi.")
    balance += 3500
    suit = "hafif"

sure = int(input("Dışarıda kalacağınız saati giriniz: "))
o2 = int(input("Tankınızdaki oksijen miktarını giriniz: "))

if suit == "hafif":
    harcama = 10
elif suit == "zirhli":
    harcama = 12
elif suit == "meka":
    harcama = 15

harcanacak = harcama * sure
sonuc = o2 - harcanacak

if sonuc < 0:
    print("Oksijen miktarı yetersiz!")
    alinabilecek = o2 / harcama 
    print(f"Kalabileceğiniz süre {alinabilecek:.2f}")
    exit() 
else:
    print("Yeterli oksijen mevcuttur")

car = input("Araç kiralamak ister misiniz? (Evet/Hayır): ").lower()

if car == "evet":
    balance -= 1500
    if balance < 0:
        print("Bakiye yetersiz. Yayan olarak gidebilirsiniz.")
        balance += 1500
        car = "hayir"

print("-" * 35)
print(f"Astronot Departmanı:\t{dep.upper()}")
print(f"Seçilen Kıyafet:\t{suit.upper()}")
print(f"Kalan Oksijen:\t\t{sonuc}")
print(f"Kalan Kredi:\t\t{balance:.2f}")
print("Durum:\t\t\tHava kilidi açılıyor. Bol şans!")
