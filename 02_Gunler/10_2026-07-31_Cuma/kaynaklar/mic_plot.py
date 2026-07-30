#!/usr/bin/env python3
"""
Gün 10 — Mikrofon ADC stream canlı grafik

Kullanım:
  pip install -r requirements.txt
  python mic_plot.py --simulate              # sahte 1 kHz sinüs (kart yok)
  python mic_plot.py --port COM5             # gerçek UART
  python mic_plot.py --port COM5 --baud 115200 --window 500

Beklenen UART formatı (her satır bir örnek):
  2048
  2101
  veya
  MIC=2048
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

LINE_RE = re.compile(r"(?:MIC\s*=\s*)?(-?\d+)", re.IGNORECASE)


def parse_sample(line: str) -> int | None:
    line = line.strip()
    if not line:
        return None
    m = LINE_RE.search(line)
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def simulate_sample(t: float, fs: float = 8000.0, f0: float = 1000.0) -> int:
    """Bias ~2048 civarı, 1 kHz sinüs (12-bit ADC taklidi)."""
    bias = 2048.0
    amp = 600.0
    value = bias + amp * np.sin(2 * np.pi * f0 * t)
    return int(np.clip(value, 0, 4095))


def open_serial(port: str, baud: int):
    try:
        import serial
    except ImportError as exc:
        raise SystemExit(
            "pyserial yok. Kur: pip install -r requirements.txt"
        ) from exc

    ser = serial.Serial(port, baudrate=baud, timeout=0.05)
    return ser


def main() -> None:
    parser = argparse.ArgumentParser(description="Mikrofon UART canlı grafik")
    parser.add_argument("--port", type=str, default=None, help="COM port (ör. COM5)")
    parser.add_argument("--baud", type=int, default=115200, help="UART baud rate")
    parser.add_argument(
        "--window",
        type=int,
        default=800,
        help="Grafikte tutulacak örnek sayısı",
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Kart yokken sahte 1 kHz sinüs üret",
    )
    parser.add_argument(
        "--sim-fs",
        type=float,
        default=8000.0,
        help="Simülasyon örnekleme frekansı (Hz)",
    )
    args = parser.parse_args()

    if not args.simulate and not args.port:
        parser.error("--port ver veya --simulate kullan")

    buf: deque[int] = deque([2048] * args.window, maxlen=args.window)
    ser = None
    t0 = time.perf_counter()
    sim_n = 0

    if not args.simulate:
        print(f"Açılıyor: {args.port} @ {args.baud}")
        ser = open_serial(args.port, args.baud)
        ser.reset_input_buffer()
    else:
        print(f"Simülasyon: 1 kHz sinüs, fs={args.sim_fs:.0f} Hz")

    fig, ax = plt.subplots(figsize=(10, 4))
    (line,) = ax.plot(range(args.window), list(buf), lw=1.2, color="#1f4e79")
    ax.set_ylim(0, 4095)
    ax.set_xlim(0, args.window - 1)
    ax.set_xlabel("örnek (son N)")
    ax.set_ylabel("ADC raw")
    title = "MIC stream — SIM 1 kHz" if args.simulate else f"MIC stream — {args.port}"
    ax.set_title(title)
    ax.axhline(2048, color="#888888", ls="--", lw=0.8, label="bias≈2048")
    ax.legend(loc="upper right")
    stats = ax.text(
        0.01,
        0.98,
        "",
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )
    fig.tight_layout()

    def poll_new_samples(max_n: int = 200) -> None:
        nonlocal sim_n
        n = 0
        if args.simulate:
            while n < max_n:
                t = sim_n / args.sim_fs
                buf.append(simulate_sample(t, args.sim_fs))
                sim_n += 1
                n += 1
            # gerçek zamana yaklaş: fazla hızlı fill olmasın
            target = (time.perf_counter() - t0) * args.sim_fs
            while sim_n < target and n < max_n * 2:
                t = sim_n / args.sim_fs
                buf.append(simulate_sample(t, args.sim_fs))
                sim_n += 1
                n += 1
            return

        assert ser is not None
        while ser.in_waiting and n < max_n:
            raw = ser.readline()
            try:
                text = raw.decode("utf-8", errors="ignore")
            except Exception:
                continue
            sample = parse_sample(text)
            if sample is not None:
                buf.append(sample)
                n += 1

    def update(_frame):
        poll_new_samples()
        y = list(buf)
        line.set_ydata(y)
        arr = np.asarray(y, dtype=float)
        mean = float(arr.mean())
        peak = float(arr.max() - arr.min())
        stats.set_text(
            f"n={len(y)}  min={arr.min():.0f}  max={arr.max():.0f}\n"
            f"mean={mean:.1f}  p2p={peak:.0f}"
        )
        return line, stats

    anim = FuncAnimation(fig, update, interval=30, blit=False, cache_frame_data=False)

    try:
        plt.show()
    finally:
        anim.event_source.stop()
        if ser is not None and ser.is_open:
            ser.close()
            print("Port kapatıldı.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
