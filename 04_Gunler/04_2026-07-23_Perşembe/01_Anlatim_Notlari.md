# Gün 04 — Anlatım Notları

**Tarih:** 2026-07-23 Perşembe  
**Konu:** IRQ + EINT + karşılaştırma

---

## Hedef öğrenme çıktıları

1. ISR'da az iş, flag, race; polling vs IRQ
2. Ortak lab: ISR'da ağır iş yok; flag/queue → main'de işle.
3. Bireysel pakette Must maddelerini bağımsız tamamlamak
4. Lab notunda karar / takılma / kanıt bırakmak

---

## Anlatım iskeleti (≈45–50 dk)

| Dk | Bölüm |
|----|-------|
| 0–5 | Dünün hatırlatması + bugünün hedefi |
| 5–20 | Kavram anlatımı |
| 20–30 | Referans kod / örnek turu (`Examples/UARTn/UARTn_Interrupt/`) |
| 30–40 | Must / Stretch ayrımı + değerlendirme |
| 40–50 | Ortak lab kickoff + sorular |

---

## Anahtar kavramlar

- ISR'da az iş, flag, race; polling vs IRQ
- Must vs Stretch
- Kanıt odaklı teslim (log / screenshot / checklist)

---

## Dikkat noktaları (mentör)

- Takılınca ipucu ver, çözüm kodunu verme.
- Gün içinde Must'un ~%70'i hedef; Stretch ayrıştırıcı.
- Tek satırlık "LED yak" tipi iş kabul değil — paket bütünlüğü beklenir.
- Secret / credential commit yasak (özellikle Hafta 4).

---

## Kaynaklar

Bu klasördeki `kaynaklar/` altına slayt, pin map, cheat-sheet eklenebilir.
