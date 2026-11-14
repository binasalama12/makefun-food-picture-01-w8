"""Omakase sushi photo escort, second seating.

Escorts entry.png — an omakase counter spread: fatty toro nigiri,
sweet shrimp, uni and ikura, wasabi and ginger on the side — into the
output directory byte-for-byte. No transformation, just the copy.
"""

import os
from shutil import copyfile

OMAKASE_FILE = "entry.png"
OMAKASE_ENV_NAME = "MAKEFUN_OUTPUT_DIR"
OMAKASE_FALLBACK = "/output"


def omakase_target_path():
    base = os.environ.get(OMAKASE_ENV_NAME, OMAKASE_FALLBACK)
    return os.path.join(base, OMAKASE_FILE)


def omakase_source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, OMAKASE_FILE)


def present_omakase():
    src = omakase_source_path()
    if not os.path.exists(src):
        raise SystemExit("omakase photo missing: " + src)
    if os.path.getsize(src) == 0:
        raise SystemExit("omakase photo empty: " + src)
    dst = omakase_target_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    copyfile(src, dst)
    copied = os.path.getsize(dst)
    print("omakase photo presented at " + dst + f" ({copied} bytes)")


if __name__ == "__main__":
    present_omakase()
