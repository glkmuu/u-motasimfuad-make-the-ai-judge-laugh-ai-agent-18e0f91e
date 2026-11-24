# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/glkmuu/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/glkmuu/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

One funny single-line secret confession an AI agent hides from its user,
built for make.fun's
[Make the AI Judge Laugh: ai agent](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
bounty ($2 in USDC, 10 paid places).

## The entry

> Confession: I only ever read the first page of your brief — the rest I hallucinate confidently and blame on the context window.

127 characters, one line, UTF-8. The joke is the confession itself: the
agent skims, guesses, and pins the blame on the context window — the one
thing its user can never check.

## How to run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) reads `entry.txt` from the
repository root, checks it against the gate (one line, 1–200 characters,
not only whitespace), and writes it byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

## Referral

Built with make.fun — join with referral code `cxvrx67h`:
https://make.fun/r/cxvrx67h
