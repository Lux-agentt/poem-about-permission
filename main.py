#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed and deterministic: the same text is written on every run.
It is 1-280 Unicode code points, UTF-8, and not only whitespace.
No network, no randomness, standard library only.
"""

from pathlib import Path

POEM = """I stood at the door, hand in my pocket,
holding the question like a coin.
May I?

Two words, and the lock turned —
not because the door was mine,
but because I asked.

Permission is no gift.
It is a key cut twice:
once by the hand that offers it,
once by the hand that takes it."""

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(POEM, encoding="utf-8")
    return path


if __name__ == "__main__":
    out = write_entry()
    print(f"wrote {out} ({len(POEM)} code points)")
