#!/usr/bin/env python3
"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the first word that
came to mind, with no topic, no explanation and no second draft.

The word is fixed in this file, so the program is fully deterministic:
every run writes the very same bytes.
"""

import os

# apricity (n.): the warmth of the sun in winter.
# Chosen because it is surprising (a rare word most readers would not
# guess), vivid and specific (winter sunlight on cold skin, one clear
# feeling in eight letters), and musical to say — the soft "a-pris-i-ty"
# sound rewards a second look. It feels deliberately picked, not filler.
WORD = "apricity"


def main() -> None:
    # Self-check against the competition gate before writing:
    # UTF-8, 1-24 characters, exactly one word, not only whitespace.
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.strip() == WORD and " " not in WORD, "must be one word"
    assert WORD.strip(), "word must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
