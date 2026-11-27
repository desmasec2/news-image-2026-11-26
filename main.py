#!/usr/bin/env python3
"""News Image 2026-11-26 — entry program for the make.fun bounty
"Sum up 26 November's world news in one image" (news-image-20261126).

The entry is the poster in entry.png beside this file: one dense page
that sums up Thursday 26 November 2026 in thirty-five dated stories
from every region. This program copies that image to the output directory,
unchanged, so the grader receives exactly the bytes in the repository
and both of its runs write identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

MAX_BYTES = 1_048_576  # the gate's 1 MiB cap for the entry image
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def entry_bytes(path):
    """Read the shipped image and check it against the gate's rules:
    a whole PNG or JPEG, told apart by its first bytes, of at most
    1 MiB. Anything else is refused before it can reach the output."""
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise SystemExit("entry.png is neither a PNG nor a JPEG by its first bytes")
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    data = entry_bytes(source)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)

    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
