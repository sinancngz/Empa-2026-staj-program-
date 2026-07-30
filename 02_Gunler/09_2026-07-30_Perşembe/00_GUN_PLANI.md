# Gün 09 — Mikrofon (ADC)

| | |
|---|---|
| **Tarih** | 2026-07-30 Perşembe |
| **Hafta** | 2 |
| **Konu** | Analog mikrofon, ADC raw okuma, UART log |
| **Referans** | `Examples/ADC/ADC_Microphone/` |

---

## Bugün ne yapacağız?

Kart üzerindeki analog MEMS mikrofonu ADC ile okuyup ham değerleri UART terminalde göstereceğiz. Sessiz / sesli ortam farkını gözlemleyeceğiz.

Anlatım notları: [`01_Anlatim.md`](01_Anlatim.md)  
Görevler: [`02_Gorevler.md`](02_Gorevler.md)

---

## Günlük ritim

| Saat | Aktivite |
|------|----------|
| 09:00–10:30 | Mikrofon + ADC anlatımı ([`01_Anlatim.md`](01_Anlatim.md)) |
| 10:30–12:30 | Şema / kanal bulma + ADC kurulum |
| 13:30–14:30 | Konu pekiştirme / mentör turu |
| 14:30–16:30 | Görevler + bonuslar |
| 16:30–17:00 | Stand-up + teslim |

---

## Anlatım özeti

- Analog mikrofon → ADC → UART zinciri  
- Pil ADC’si ile fark: AC sinyal, bias (orta nokta)  
- Raw → voltaj  
- Örnekleme (kısa); yarın 1 kHz + Python grafik önizlemesi  

Detay: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görevler

Herkes aynı listeyi yapar.  
Detay: [`02_Gorevler.md`](02_Gorevler.md)

Özet kabul:

- Mikrofon ADC değeri okunuyor  
- UART’ta `MIC = …` görünüyor  
- Sessiz / sesli fark gözlemleniyor  
- Voltaj dönüşümü raporda var  

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md
└── proje/
```
