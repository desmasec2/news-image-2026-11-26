#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261126 bounty.

The repository ships the finished poster as entry.png. When the grader
runs this program it simply delivers that image to the output folder,
byte for byte, so the picture judged is exactly the one in the repo:
one dense front page of 35 dated stories from Thursday 26 Nov 2026.

A local run looks like:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

from pathlib import Path
import os
import sys

LIMIT = 1024 * 1024  # the gate allows at most 1 MiB
SIGNATURES = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff")  # PNG, JPEG


def load_poster() -> bytes:
    """Read the poster beside this file and check it against the gate:
    a PNG or a JPEG by its first bytes, and no larger than the cap."""
    poster = Path(__file__).with_name("entry.png")
    blob = poster.read_bytes()
    if len(blob) > LIMIT:
        sys.exit(f"poster too large: {len(blob)} bytes (limit {LIMIT})")
    if not blob.startswith(SIGNATURES):
        sys.exit("poster is not a PNG or JPEG image")
    return blob


def deliver(blob: bytes) -> Path:
    """Write the poster into the output folder as entry.png."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"
    target.write_bytes(blob)
    return target


if __name__ == "__main__":
    image = load_poster()
    written = deliver(image)
    print(f"entry.png delivered to {written} ({len(image)} bytes)")
