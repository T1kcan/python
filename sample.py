my_dict = {"elma": 5, "armut": 3, "muz": 2}

def sozluk(kelimeler):
    for key in kelimeler:
        print(kelimeler[key])

print(sozluk(my_dict))

def sirala_degerlere_gore(liste):
  # String formatındaki sözlükleri gerçek sözlüklere dönüştürme
  sozlukler = []
  for eleman in liste:
      anahtar, deger = eleman.split(':')
      sozlukler.append({anahtar: int(deger)})

  # Değerlere göre sıralama (büyüktten küçüğe)
  sirali_sozlukler = sorted(sozlukler, key=lambda x: list(x.values())[0], reverse=False)

  return sirali_sozlukler

# Örnek kullanım
tickets = ['T123:4', 'T124:1', 'T125:3', 'T126:5', 'T127:3']
sonuc = sirala_degerlere_gore(tickets)
print(sonuc)