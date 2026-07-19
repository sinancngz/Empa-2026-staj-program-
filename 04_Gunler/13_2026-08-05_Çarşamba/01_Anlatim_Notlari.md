# Gün 13 — Anlatım Notları

**Tarih:** 2026-08-05 Çarşamba  
**Konu:** Multi-sensor orchestration

---

## Hedef öğrenme çıktıları

1. Birden fazla sensörü aynı loop'ta yönetme
2. Ortak lab: Kısmi fail'de diğer sensör devam; öncelik kuralları.
3. Bireysel pakette Must maddelerini bağımsız tamamlamak
4. Lab notunda karar / takılma / kanıt bırakmak

---

## Anlatım iskeleti (≈45–50 dk)

| Dk | Bölüm |
|----|-------|
| 0–5 | Dünün hatırlatması + bugünün hedefi |
| 5–20 | Kavram anlatımı |
| 20–30 | Referans kod / örnek turu (`Examples/TiremoCortex/` + I2C + ADC örnekleri) |
| 30–40 | Must / Stretch ayrımı + değerlendirme |
| 40–50 | Ortak lab kickoff + sorular |

---

## Anahtar kavramlar

- Birden fazla sensörü aynı loop'ta yönetme
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
