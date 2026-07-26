# Gün 07 — Görevler (Pil voltajı okuma)

Anlatım: [`01_Anlatim.md`](01_Anlatim.md)

---

## Görev

Pilden voltaj oku. Hesapladığın değeri (mV veya V) **debug UART / terminalde her 5 saniyede bir** yazdır.

Örnek satır:

```text
BAT = 3720 mV
```

(istersen yanına `raw` de ekleyebilirsin)

### Yapılacaklar

| # | Madde | Yapıldı |
|---|-------|---------|
| 1 | Şema + datasheet’ten pil pin / ADC kanalını bul (rapora yaz) | ☐ |
| 2 | ADC ile pil kanalından ölçüm al | ☐ |
| 3 | `raw` → voltaj (mV/V) çevir; bölücü varsa uygula | ☐ |
| 4 | Terminalde **5 saniyede bir** pil değerini göster | ☐ |
| 5 | Aşağıdaki teorik soruları rapora cevapla | ☐ |

### Kabul

Mentöre gösterirken terminalde yaklaşık 5 sn arayla güncellenen pil değeri görünmeli.

---

## Teorik sorular (cevapları rapora yaz)

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
├── rapor/gunluk_rapor.md   ← pin/kanal, formül, teorik cevaplar
└── proje/
```
