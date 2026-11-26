"""Rename the Planet entry: write one funny one-liner to /output/entry.txt.

The line renames Mars "The Landlord" and earns the name from Mars's own
traits: the whole planet is rust-red, its dust storms fill everything, and
— the reversal — its sunsets are blue. One scene (a landlord's flat), one
reversal (blue sunsets on a red planet), one landing line (keeping the
deposit). 143 characters, under the 200-character gate.
"""

import os
from pathlib import Path

ENTRY = (
    'Rename Mars "The Landlord": it painted the whole planet rust, fills '
    "every room with dust, and its sunsets are blue \u2014 just to keep "
    "your deposit."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate takes 1-200 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry outside the gate"

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(ENTRY, encoding="utf-8")
