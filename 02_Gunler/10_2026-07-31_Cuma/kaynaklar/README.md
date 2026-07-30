# Gün 10 — Kaynaklar

| Dosya | Ne için? |
|-------|----------|
| [`mic_plot.py`](mic_plot.py) | UART / simülasyon canlı mikrofon grafiği |
| [`requirements.txt`](requirements.txt) | `pyserial`, `matplotlib`, `numpy` |
| [`../01_Anlatim.md`](../01_Anlatim.md) | Teori (stream, Nyquist, 1 kHz) |
| [`../02_Gorevler.md`](../02_Gorevler.md) | Görev checklist |

## Hızlı başlangıç

```bash
cd 02_Gunler/10_2026-07-31_Cuma/kaynaklar
pip install -r requirements.txt
python mic_plot.py --simulate
python mic_plot.py --port COM5 --baud 115200
```

COM numarasını Windows Aygıt Yöneticisi’nden öğren.
