import winsound
import msvcrt
import time
import os

os.system("")

# Color codes
colors = [
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[91m",  # Red
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m"   # Cyan
]

reset = "\033[0m"

print("🎧 A–Z Drum Machine")
print("Press A–Z or a–z for beats")
print("Press ENTER to exit\n")

duration = 100  # base ms

# --- Beat Names ---
beat_names = [
    "Kick", "Snare", "Clap", "Hi-Hat", "Tom Low", "Tom Mid",
    "Tom High", "Rimshot", "Cowbell", "Shaker", "Block",
    "Click", "Blip", "Zap", "Ping", "Pop", "Pluck",
    "Tick", "Knock", "Wood", "Chirp", "Bell", "Laser",
    "Echo", "Drop", "Whip"
]

# --- Build frequency + wave effects ---
beats = {}

base_freq = 180
step = (1500 - 180) // 25

for i in range(26):
    letter_low = chr(ord('a') + i).encode()
    letter_up = chr(ord('A') + i).encode()

    freq = base_freq + (i * step)
    name = beat_names[i]

    # Wave effect: each beat gets 1, 2, or 3-tone pattern
    pattern = [
        (freq, duration),
        (freq + 50, duration // 2),
        (freq - 30, duration // 2)
    ] if i % 3 == 0 else (
        [(freq, duration), (freq + 80, duration // 2)]
    ) if i % 3 == 1 else (
        [(freq, duration)]
    )

    beats[letter_low] = (i + 1, name, pattern)
    beats[letter_up] = (i + 1, name, pattern)


# --- Pulse Animation ---
def pulse_bar(color_index, length=20):
    bar = colors[color_index] + "█" * length + reset
    print(bar)


# --- Main Loop ---
color_index = 0

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        # ENTER = exit
        if key == b'\r':
            print("\n🎶 Closed with ENTER.")
            break

        if key in beats:
            num, name, pattern = beats[key]

            # Play multi-tone pattern
            for (freq, dur) in pattern:
                winsound.Beep(freq, dur)

            # Color pulse
            pulse_bar(color_index, length=10 + (num % 10))

            # Print info
            print(f"{colors[color_index]}Beat {num} ({name}){reset}")

            # Rotate colors
            color_index = (color_index + 1) % len(colors)

    time.sleep(0.01)
