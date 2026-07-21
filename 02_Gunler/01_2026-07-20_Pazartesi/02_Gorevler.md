# Gün 01 — GPIO Görevleri

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitince çalışmanı göster / teslim et.

Referans: `Examples/GPIO/*` · `GPIO_LEDBlinky` · Anlatım: [`01_GPIO_Anlatim.md`](01_GPIO_Anlatim.md)

---

## Ortak hazırlık

- [ ] ABOV ortamı kurulu (eMStudio32 açılıyor)
- [ ] Kart USB-C ile bağlı
- [ ] Projeyi açabildin / oluşturabildin
- [ ] GPIO notunu okudun

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
| En az 3 LED kayan ışık (chase); butonla yön **veya** hız değiştir; başlangıçta kısa self-test. Bitince kendi **GitHub** reponu oluşturup bugünün tarihli klasörüne yükle | ☐ |

**Beklenen:** Birden fazla pin + basit sayaç / durum. Kartta göster; repo linkini rapora yaz.

### GitHub teslimi (zor — kendi repon)

1. GitHub’da **kendi** staj reponu oluştur (örn. `empa-2026-staj` — isim serbest).  
2. Bugünün işini **günün tarihiyle** yükle:

```
YYYY-MM-DD/
└── ...
```

Bugün: **`2026-07-20`**

3. README’de kısaca ne yaptığını yaz; repo URL’sini günlük rapora ekle.

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md    ← GitHub repo URL’si
└── proje/
```

Ayrıca: zor görev → kendi GitHub repon (`2026-07-20/`).
