"""One Word for Your Wi-Fi — make.fun entry.
"Ghosting" fits because your Wi-Fi disappears on you mid-call,
just like a bad date — instantly understood, and it works
perfectly as a network name.
Writes one Wi-Fi word (8 characters) to /output/entry.txt.
"""

import os

MAX_LEN = 20

# Joke angle: the network ghosts you mid-call, vanishing without a word.
LINE = "Ghosting"

assert 1 <= len(LINE) <= MAX_LEN, "line out of gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    content = f.read()

assert content == LINE
