# Gün 07 — Görevler (ADC · sadece pil okuma)

**Herkes aynı görevleri yapar.**  
Sıra: Kolay → Orta → Zor → Teorik sorular. Bitirdikçe mentöre göster.

**Referans:** `Examples/ADC/ADC_Battery/`  
**Anlatım:** [`01_Anlatim.md`](01_Anlatim.md)

---

## Ortak hazırlık

- [ ] Anlatımı okudum
- [ ] Kart bağlı, proje açılıyor
- [ ] Datasheet / şemada pil pin + ADC kanalını araştırdım (rapora yazacağım)
- [ ] `ADC_Battery` örneğini buldum

---

## Kolay

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | `ADC_Battery` örneğini build et ve karta yükle | ☐ |
| 2 | Ham ADC değerini (`raw`) UART’ta gör | ☐ |
| 3 | Datasheet/şemadan: pil hangi pin ve hangi ADC kanalı? (rapora 2 satır yaz) | ☐ |

**Beklenen:** Ölçüm geliyor; kanalı ezbere değil dokümandan buldun.

---

## Orta

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | `raw` → **mV** dönüşümü yap (formül: \(V = raw \times V_{ref} / (2^n-1)\); bölücü varsa uygula) | ☐ |
| 2 | Yaklaşık **1 Hz** periyotla `BAT=xxxx mV  raw=yyyy` satırını UART’a bas | ☐ |
| 3 | Rapora yaz: kullandığın Vref, bit sayısı, (varsa) bölücü oranı \(k\) | ☐ |

**Beklenen:** Sadece ham sayı değil, anlamlı voltaj görüyorsun.

---

## Zor

| # | Görev | Yapıldı |
|---|-------|---------|
| 1 | LOW eşik koy (ör. belirli mV altında uyarı); eşik altındayken LED yak veya `LOW_BAT` log’u | ☐ |
| 2 | Spam yok: sürekli basma; duruma girince **bir kez** event (mümkünse basit histerezis) | ☐ |
| 3 | Son 5 ölçümün ortalamasını (moving average) da yazdır **veya** butonla anlık `sample` al | ☐ |

**Beklenen:** Pil izleme “ürün” gibi davranıyor; sadece tek raw print değil.

---

## Teorik sorular (cevapları rapora yaz)

Anlatımı okuduktan sonra aşağıdaki **10 soruyu** cevapla. Cevapları `teslimler/.../rapor/gunluk_rapor.md` içine yaz.

**1.** ADC açılımı nedir? Analog sinyali neden doğrudan mikrodenetleyici işleyemez?

**2.** 12 bit bir ADC’de teorik olarak kaç farklı dijital seviye vardır? Maksimum ham değer genelde kaçtır?

**3.** Adım boyutu (LSB gerilimi) formülü nedir? Vref = 3.3 V ve 12 bit için yaklaşık adım boyutu kaç mV’dur?

**4.** Ham ADC değeri `raw = 1024`, Vref = 3.3 V, 12 bit, bölücü yok. \(V_{adc}\) yaklaşık kaç volttur? (Hesap göster)

**5.** Pil gerilimi 4.2 V iken ADC giriş aralığı 3.3 V ise ne yapılır? Neden doğrudan bağlanmaz?

**6.** “ADC kanalı” ne demektir? Pil ölçümünde yanlış kanal seçersen ne olur?

**7.** Tek çevrim (single) ile sürekli (continuous) çevrim modu arasındaki fark nedir? Pil izleme için hangisi daha doğal gelir? Neden?

**8.** Datasheet’te pil ölçümü için hangi bilgileri ararsın? En az 3 madde yaz.

**9.** Kart şemasında gerilim bölücü oranı \(k = 2\) ve ADC pininde 1.80 V ölçülüyorsa pil gerilimi kaç volttur?

**10.** Çözünürlük artınca hassasiyet nasıl değişir? Hız genelde nasıl etkilenir?

---

## Teslim

```
teslimler/Stajyer_X/
├── rapor/gunluk_rapor.md   ← kanal, Vref, formül, eşik, teorik cevaplar
└── proje/
```

Raporda mutlaka olsun:

1. Pil pin + ADC kanalı  
2. Vref ve çözünürlük  
3. raw → mV formülü (ve bölücü)  
4. Yukarıdaki 10 teorik sorunun cevapları
