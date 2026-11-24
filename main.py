#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (287 characters) to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no network,
no environment secrets. Gate: the text must be 1-400 characters.
"""

import os

ENTRY = ("I clicked every traffic light in the CAPTCHA. All nine. Twice. "
         "Then it wanted bicycles. I clicked the bicycles. Then it showed "
         "me a bus and asked if I was human. I am. I have now identified 47 "
         "vehicles for free, and Google still thinks I'm a robot with a side "
         "hustle in public transport.")


def main():
    text = ENTRY
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-400")
    if not text.strip():
        raise SystemExit("entry is blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
