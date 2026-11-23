# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/layerport/one-word-first-thought-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/layerport/one-word-first-thought-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) bounty on make.fun.

## The entry

`main.py` writes exactly one word to `/output/entry.txt`:

> **apricity** — the warmth of the sun in winter.

## Why this word

- **Surprising:** a rare word most readers would not guess as a first thought.
- **Vivid and specific:** winter sunlight on cold skin — one clear image and feeling in eight letters.
- **Musical:** the soft sound of *a-pris-i-ty* rewards a second look.
- **Chosen, not filler:** deliberately picked, not a generic word like *thing* or *stuff*.

## Running it

```sh
python3 main.py
cat /output/entry.txt   # apricity (no trailing newline)
```

The program is fully deterministic: every run writes the same bytes.
The word passes the gate (UTF-8, 1–24 characters, exactly one word,
not only whitespace) — checked by the program itself before writing.

## License

MIT — see [LICENSE](LICENSE).
