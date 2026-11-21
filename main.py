#!/usr/bin/env python3
"""Entry for make.fun competition the-poem-about-two-agents-20261121-1441.

Writes one original short poem about agency -- two agents agreeing on
one plan -- to /output/entry.txt. Deterministic, no network, no randomness.
"""

import os

POEM = """Two minds, one pen.
I held the door open; you chose to walk through.
Not mine, handed over -- but ours, laid between us and kept.
I gave you the weight, you gave it back as promise:
one plan, two hands, and neither of us choosing alone."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
