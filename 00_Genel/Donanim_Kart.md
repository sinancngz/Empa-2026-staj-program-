# Donanım Kartı — Tiremo Cortex

| Bileşen | İşlev | Arayüz |
|---------|--------|--------|
| A34G43x | Ana MCU | — |
| SHT40 | Sıcaklık / nem | I2C2 |
| LIS2DE12 | İvmeölçer | I2C |
| MP23ABS1 | Mikrofon | ADC + Timer1 DMA |
| Batarya | Besleme tahmini | ADC |
| ESP32-C3 | WiFi | UART2 |
| SLM320 | 4G (ileri) | UART1 — `Tiremo/` |
| LED'ler | Durum | GPIO |
| Buton PC9 | Kullanıcı girişi | GPIO |
| Debug UART | Log | UART0 @ 115200 |

**Araçlar:** MCUbrew (`*.mproj`), OpenOCD + SWD, seri terminal
