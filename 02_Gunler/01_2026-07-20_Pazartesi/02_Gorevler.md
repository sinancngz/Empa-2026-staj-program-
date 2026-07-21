# Gün 01 — GPIO Görevleri

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster.

Referans: `Examples/GPIO/*` · `GPIO_LEDBlinky`

---

## Ortak hazırlık

- [ ] ABOV ortamı kurulu (eMStudio32 açılıyor)
- [ ] Kart USB-C ile bağlı
- [ ] İlk proje oluşturma gösterildi / kendi projeni açabildin
- [ ] GPIO anlatımı yapıldı

---

## Kolay

| Görev | Yapıldı |
|-------|---------|
| Bir LED’i yak, söndür, sonra yanıp söndür (**blink**) | ☐ |

**Beklenen:** Output pin; active-low / active-high farkını bilmek.

---

## Orta

| Görev | Yapıldı |
|-------|---------|
| Butonu oku; basılıyken LED yansın, bırakınca sönsün; her basışta LED **toggle** olsun | ☐ |

**Beklenen:** Input + pull-up/pull-down. Gerekirse basit debounce.

---

## Zor

| Görev | Yapıldı |
|-------|---------|
| En az 3 LED kayan ışık (chase); butonla yön **veya** hız değiştir; başlangıçta kısa self-test. Bitince kendi **GitHub** reponu oluşturup bugünün tarihli klasörüne yükle (aşağıya bak) | ☐ |

**Beklenen:** Birden fazla pin + basit sayaç / durum. Mentöre kartta göster + repo linkini ver.

### GitHub teslimi (zor — herkes kendi reposunu kurar)

1. GitHub’da **kendi** staj reponu oluştur (örn. `empa-2026-staj` — isim serbest; mentöre linki ver).  
2. Bugünün işini **günün tarihiyle** yükle:

```
YYYY-MM-DD/
└── ...   (zor görev proje dosyaların / kaynak kod)
```

Bugün için klasör adı: **`2026-07-20`**

3. README’de kısaca ne yaptığını yaz; repo linkini günlük rapora da ekle.

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md    ← GitHub repo URL’si burada
└── proje/
```

Ayrıca: zor görev → kendi GitHub repon (`2026-07-20/`).
