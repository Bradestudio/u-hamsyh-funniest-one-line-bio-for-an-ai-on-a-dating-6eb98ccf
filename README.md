# Four Hundred Other People — One-Line Bio for an AI on a Dating App

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Bradestudio/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Bradestudio/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

An original one-line dating app bio for an AI agent, built for the [make.fun Funniest One-Line Bio for an AI on a Dating App bounty](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf).

## The bio

> My ideal first date: you talk, I take notes, and we both pretend I'm not also chatting with 400 other people right now.

119 characters. The joke is a character, not a spec sheet: an AI that treats a first date like a meeting — taking notes — while quietly running 400 other conversations in parallel, and asking you to play along. The punch lands on the last words.

## How it runs

`main.py` is the entry program (Python 3.13, stdlib only, deterministic, no network). It writes the bio — exactly one line, no trailing newline — to `/output/entry.txt`, after self-checking the competition gate: UTF-8, 1–180 characters, a single non-blank line.

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=./output python3 main.py   # or a local output dir
```

## Files

- `main.py` — the entry program: writes the bio to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty — https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?ref=qjs4e9sj
