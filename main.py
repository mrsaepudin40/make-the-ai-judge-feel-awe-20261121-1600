"""Write one short relaxing text to /output/entry.txt.

The text is a fixed constant: no network, no randomness, no clock,
so every run writes the same bytes. It is 1-280 Unicode code points,
so it passes the gate as written.
"""

from pathlib import Path

TEXT = (
    "One by one, the stars come out over the field, small, steady, "
    "until the dark is full of them. The grass is cool underfoot, and "
    "the night air smells of rain that has already passed. Above, the "
    "sky keeps opening, star by star, long after the last one you counted."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
