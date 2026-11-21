"""Write one short relaxing text to /output/entry.txt.

The text is a fixed constant: no network, no randomness, no clock,
so every run writes the same bytes. It is 1-280 Unicode code points,
so it passes the gate as written.
"""

from pathlib import Path

TEXT = (
    "You are small.\n"
    "Your father carries you\n"
    "on his shoulders,\n"
    "his hand on your ankle.\n"
    "\n"
    "The road winds home below.\n"
    "The stars come out above.\n"
    "\n"
    "Their light left\n"
    "before the road was built,\n"
    "before the first house stood,\n"
    "and only now reaches you,\n"
    "while you are still awake."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
