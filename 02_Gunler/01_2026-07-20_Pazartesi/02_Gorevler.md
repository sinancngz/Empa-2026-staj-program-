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

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Bir LED’i sabit yak | yapıldı |
| 2 | Aynı LED’i söndür | yapıldı |
| 3 | LED’i yanıp söndür (blink) | yapıldı |

**Beklenen:** Output pin ve active-low / active-high farkı.

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Kullanıcı butonunu oku (basılı / değil) | yapıldı |
| 2 | Buton basılıyken LED yansın, bırakınca sönsün | yapıldı |
| 3 | Buton her basışta LED’i aç/kapa (toggle) | yapıldı |

**Beklenen:** Input + pull-up/pull-down. Gerekirse basit debounce.

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | En az 3 LED’i sırayla yak (chase / kayan ışık) | ☐ |
| 2 | Butonla yön veya hız değiştir (ileri ↔ geri **veya** yavaş ↔ hızlı) | ☐ |
| 3 | Başlangıçta kısa self-test: tüm LED’ler bir kez yanıp sönsün | ☐ |

**Beklenen:** Birden fazla pin + basit sayaç / durum.

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
