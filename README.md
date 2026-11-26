# Museum of the Year 3000

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/hupo3661/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/hupo3661/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)


A make.fun entry for
[u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb):
write the museum label a museum in the year 3000 puts beside an
ordinary object from today — one line, at most 200 characters. Our
object is a plastic fork from 2025.

## The label

> Plastic fork, 2025: a single-use eating tool from the Age of Convenience, when humans threw away forever-objects after a single lunch.

134 characters, one sentence, one line. The label is also kept on
its own in `entry.txt`, exactly as submitted.

## Why a fork

The fork is the perfect exhibit for the year 3000: an object built
to last forever, used once, and thrown away. The label's sting is in
its last words — "forever-objects after a single lunch" — a whole
civilisation's attitude to waste in seven words.

## What the program does

`main.py` is a small label press:

- **Rules as data** — every contest rule is a named test in one
  list, so adding or reading a rule means touching one place. The
  label is checked against all of them at once and every broken
  rule is reported together.
- **Mounting** — the label is written to `/output/entry.txt` and
  read straight back; the mounted copy must match the approved
  text character for character, trailing newline included.
- **Flexible destination** — `--output <path>` wins, otherwise the
  `OUTPUT_PATH` environment variable, otherwise the default.

## Run it

```sh
python3 main.py
```

Prints the label and mounts it at `/output/entry.txt`. More ways to
run it:

```sh
python3 main.py --verify-only              # check the label, write nothing
python3 main.py --output /tmp/label.txt    # mount it somewhere else
OUTPUT_PATH=/tmp/label.txt python3 main.py # same, via environment
python3 main.py --quiet                    # mount it, print nothing
```

Only the Python 3 standard library is used. No network, no clock,
no randomness — the same run always mounts the same label.

## Files

- `main.py` — the label, its rules, and the mounting step.
- `entry.txt` — the label alone, verbatim.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
