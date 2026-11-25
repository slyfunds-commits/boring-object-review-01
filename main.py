"""Boring Object Review — make.fun entry.

Writes the keeper line to /output/entry.txt, exactly, with no trailing newline.
Pure stdlib; the grader runs python:3.13-slim with no site-packages.
"""

import os

# The turn: the coaster prevents the ring by being the ring — the preventer IS the cause.
# The ring detail belongs to the coaster alone; the last words sharpen the turn.
# Gate: 1-200 chars UTF-8; keeper is 104 chars, pure ASCII, one line.
ENTRY = "One star. It prevents the ring. It leaves a ring. The ring is from the coaster. The coaster is the ring."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
