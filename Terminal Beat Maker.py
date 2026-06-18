import winsound
import msvcrt
import time

print("🎧 A–Z Beats (1 to 26)")
print("Press A–Z or a–z for beats")
print("Press ENTER to exit\n")

duration = 120  # milliseconds

# Build frequency table + beat numbers
beats = {}

start_freq = 200
step = (1500 - 200) // 25  # smooth rise across 26 letters

for i in range(26):
    lower = chr(ord('a') + i).encode()
    upper = chr(ord('A') + i).encode()
    freq = start_freq + (i * step)
    beats[lower] = (i + 1, freq)
    beats[upper] = (i + 1, freq)

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        # ENTER key = close program
        if key == b'\r':
            print("\n🎶 Program closed with ENTER.")
            break

        if key in beats:
            number, freq = beats[key]
            winsound.Beep(freq, duration)
            print(f"Beat {number} ({key.decode()}) → {freq} Hz")

    time.sleep(0.01)
