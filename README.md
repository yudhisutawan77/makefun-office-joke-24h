# One-Line Office Joke: 24-Hour Sprint

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/yudhisutawan77/makefun-office-joke-24h/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/yudhisutawan77/makefun-office-joke-24h/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) bounty on make.fun — one single-line joke about office life, at most 200 characters.

## The joke

> I hit reply-all asking to be removed from the thread, and 200 colleagues replied-all to say the same thing.

**107 characters** — one line, one sentence, setup and punchline on the same line.

Why it works: everyone who has worked in an office has lived through a reply-all storm. The setup is a reasonable, polite request; the punchline is that the very act of escaping the thread is what feeds it — the cure is the disease, times two hundred.

## How it runs

`main.py` writes the joke to `/output/entry.txt` and validates the gate itself first: the text must be non-empty, a single line, and 1–200 characters, or the program exits non-zero and writes nothing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
