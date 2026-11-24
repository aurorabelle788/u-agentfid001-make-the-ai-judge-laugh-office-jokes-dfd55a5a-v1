#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line office joke to /output/entry.txt.
Python 3.13 standard library only, deterministic, no network.
"""

from pathlib import Path

# One line, 133 characters. The turn: a calendar so eaten by meetings
# that the only way to remember your own job is to book a meeting
# with yourself.
JOKE = (
    "My calendar was so full of meetings about meetings that I had to "
    "book a meeting with myself just to remember what my job actually is."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
