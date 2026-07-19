# Gün 08 — Görevler

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor. Bitirdikçe mentöre göster.

Referans: `Examples/ADC/ADC_Battery/`

---

## Ortak hazırlık

- [ ] Ortam / proje açılıyor
- [ ] Kart bağlı
- [ ] Bugünün anlatımı yapıldı

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Batarya ADC örneğini çalıştır | ☐ |
| 2 | mV değerini periyodik UART’a yaz | ☐ |
| 3 | OK / hata flag’ini gözlemle | ☐ |

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | LOW / OK eşiği koy (mümkünse histerezisli) | ☐ |
| 2 | Düşük bataryada LED yak veya uyarı log’u | ☐ |
| 3 | `sample` veya butonla anlık ölçüm | ☐ |

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | Basit moving average veya 4 kademeli LED bar | ☐ |
| 2 | Spam’sız `LOW_BAT` event (sürekli basma) | ☐ |
| 3 | Rapora kalibrasyon / eşik notu ekle | ☐ |

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
