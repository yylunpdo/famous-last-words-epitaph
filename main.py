#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph (at most 150 characters)
to /output/entry.txt. Pure Python standard library, fully deterministic.
"""

import os

EPITAPH = "Here lies Greg. He asked the universe for a sign. It sent a bus."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 150


def main() -> None:
    text = EPITAPH.strip()
    assert "\n" not in text, "epitaph must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"epitaph must be 1-{MAX_CHARS} characters, got {len(text)}"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
