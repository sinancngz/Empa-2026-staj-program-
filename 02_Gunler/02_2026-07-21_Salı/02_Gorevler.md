# Gün 02 — Görevler

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster.

Referans: `Examples/GPIO/*`

---

## Ortak hazırlık

- [ ] Ortam / proje açılıyor
- [ ] Kart bağlı
- [ ] Bugünün anlatımı yapıldı

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Butonu oku (basılı / değil) ve LED ile göster | ☐ |
| 2 | Basit debounce ekle (gecikme veya ardışık okuma) | ☐ |
| 3 | Her basışta UART veya LED ile bir kez tepki ver (spam yok) | ☐ |

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Kısa basış ve uzun basış ayır (ör. 1 sn eşik) | ☐ |
| 2 | Kısa basış → LED toggle | ☐ |
| 3 | Uzun basış → farklı LED pattern veya tüm LED flash | ☐ |

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | PRESS / RELEASE / LONG event üret (basit state) | ☐ |
| 2 | En az 2 LED davranışını event’lere bağla | ☐ |
| 3 | İsteğe bağlı: çift tık (DOUBLE) veya basılı tutma süresi göstergesi | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
