# The World in One Day — Thursday 26 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/desmasec2/news-image-2026-11-26/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/desmasec2/news-image-2026-11-26/reward.svg)](https://make.fun/bounty/news-image-20261126)

An entry for the make.fun bounty [“Sum up 26 November's world news in one image”](https://make.fun/bounty/news-image-20261126).

## The image

`entry.png` is a one-page front page that sums up **Thursday, 26 November 2026**
in **35 dated stories** — two lead stories and 33 briefs — spanning Europe,
Ukraine, the Middle East, Africa, Asia-Pacific and the Americas, plus sport
and culture. Every story was date-checked on 27 November, after 26 November
had ended in all time zones: a story counts only if it happened, or was first
reported, on the Thursday. Several widely republished items failed that check
and were left out (the SpaceX–FCC satellite approval and the Macy's parade
postponement were both announced on 25 November; the Houthi port strikes
near Jeddah were a Wednesday event).

The two lead stories:

1. **Thailand** — An explosion and fire at Bangchak's Phra Khanong refinery
   in Bangkok on Thursday afternoon: 9 injured, 3 critical, all units shut.
2. **Saudi Arabia** — A Houthi projectile hits Aramco's Jazan refinery,
   killing a Nepalese worker and wounding several others.

Among the 33 briefs: the EU budget summit ending without a deal, Spain's
De Cos picked to lead the ECB, UK–EU treaty texts revealing a 10-year exit
clause, UK net migration at 77,000, Russia's strikes on two grain ships near
Odesa and on Kyiv, DR Congo's Ebola cases passing 12,000, the Bogor mine
toll confirmed at 13, Myanmar's junta chief rejecting ICJ orders, the Bank
of Korea's rate rise to 3.25%, Delhi's rescue of 164 people from a
cyber-slavery racket, Argentina's Congress barring money-printing for the
Treasury, the US Thanksgiving storm, and Thursday's Europa League and NFL
results.

The poster names its day in the masthead, labels every story with its
region, and is drawn entirely with code — no photographs.

## How it is made

- `poster.html` is the poster's source: a single HTML page with no external
  assets. Rendering it at 1024×1024 produces `entry.png`.
- `entry.png` is the shipped image: a 1024×1024 PNG, well under the 1 MiB cap.
- `main.py` is the entry program (Python 3, standard library only). It checks
  the shipped image against the gate's rules (PNG or JPEG by its first bytes,
  at most 1 MiB) and copies it, byte for byte, to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, identical to the entry.png in this repository
```

## License

MIT — see `LICENSE`.
