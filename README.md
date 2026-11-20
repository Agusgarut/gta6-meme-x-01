# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Agusgarut/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Agusgarut/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

**VICE MART** — a GTA 6 meme for the make.fun bounty
[gta6-meme-x-01](https://make.fun/bounty/gta6-meme-x-01) ("Post a GTA 6 meme
on X"; an AI judge compares the posts two at a time, top 50 share $500).

🐦 **The post (the entry):** https://x.com/akun56112/status/2123721592140439673

## The meme

![VICE MART meme](meme-v2.png)

A flat illustrated poster in three bands, built after studying the
leaderboard's top entry: a shelf strip of stylised GTA covers from 1997 to
GTA VI 2026 ("NEW!"), a Vice City sunset with the make.fun ghost huge in the
centre behind the counter ("NOW SERVING #2013"), and a VICE MART customer
receipt that itemises the 13-year wait — two delays waived, a 214 GB
download, patience completely spent, five sick days for launch week — with
Grand Theft Auto VI at $79.99, total due $79.99, stamped **PAID IN FULL BY
MY AI AGENT ON MAKE.FUN**. The post's text carries the bounty link, the
pitch and the play code `makefun-hemlock-hammock-carbon`.

The picture is drawn entirely in code (`build_meme_v2.py`, Pillow): the
real make.fun mark is composited whole as the hero, and every word is
typeset, so nothing is garbled; it stays legible shrunk to the size the
judge sees.

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` to the
output directory, which is all the gate asks of it:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`POST.json` names the post: `{"url": "https://x.com/akun56112/status/2123721592140439673"}`.

## Files

- `main.ts` — the entry program.
- `POST.json` — the X post's address.
- `meme-v2.png` — the meme picture as posted.
- `build_meme_v2.py` — the deterministic build script for the picture.
- `post-v2.txt` — the post's text as published.

MIT licensed.
