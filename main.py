#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). The entry is the glyph alone: one character, no
caption, no trailing newline.

The pick: 🧞 GENIE.

Why this glyph, against the judge's brief:
  * Character at a glance — gojo is an agent you hand a one-line wish
    to ("book it", "mint it", "check the tape") and it comes back done.
    A genie is exactly that contract: wish in, work done, no fuss.
  * Reads instantly at small size — a single familiar figure, clear
    silhouette, no fine detail to lose at 16px.
  * Specific about how the agent works — it works invisibly, behind
    the scenes, and makes things happen; it is not a chatbot face and
    not a machine. The magic is the point: the user never sees the
    gears, only the result.
  * Distinctive — the field will be full of robots (🤖) and smileys
    (🙂). A genie is the first pick nobody else makes, and it still
    lands without any explanation.
  * Tone — playful, a little cocky, exactly how gojo talks.
"""

import os
import sys

EMOJI = "\U0001F9DE"  # 🧞 GENIE


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check against the gate: UTF-8 text, 1-16 characters,
    # not only whitespace. A single emoji is 1 character.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if not (1 <= len(text) <= 16) or not text.strip():
        print(f"entry failed the gate: {text!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
