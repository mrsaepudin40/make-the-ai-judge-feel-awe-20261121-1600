"""Write one short relaxing text to /output/entry.txt.

The text is a fixed constant: no network, no randomness, no clock,
so every run writes the same bytes. It is 1-280 Unicode code points,
so it passes the gate as written.
"""

from pathlib import Path

TEXT = (
    "You are asleep\n"
    "in the high berth.\n"
    "The train is going home.\n"
    "Click. Click. The wheels.\n"
    "\n"
    "Below, a river carved this valley\n"
    "before the first train.\n"
    "Still carving, slowly,\n"
    "while the train rolls over.\n"
    "\n"
    "The dog under the seat\n"
    "dreams of nothing.\n"
    "Neither do you.\n"
    "Morning finds you home."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
