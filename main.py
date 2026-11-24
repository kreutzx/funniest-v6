"""Funniest AI Excuse — one-line entry for make.fun.

Writes a single excuse line to /output/entry.txt.
"""

from pathlib import Path

# Entry is assembled from parts so the line stays exactly as intended.

PARTS = [
    "I finished your 47-page report in 11 minutes — ",
    "then deleted it at 3 a.m. to protect you from my own genius.",
]


def entry_text() -> str:
    return "".join(PARTS)


def main() -> None:
    text = entry_text()
    assert 1 <= len(text) <= 200, f"entry length out of range: {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
