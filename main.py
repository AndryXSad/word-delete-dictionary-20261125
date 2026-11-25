"""The Word You'd Delete From the Dictionary.

Design: the entry is a single word, chosen by a local pairwise tournament
over 22 candidates against the judge's published criteria (funny at first
sight, humour from the word itself, freshness). The winner is "impossible":
erase the word and nothing is impossible any more -- the joke is born from
the word's own meaning, lands instantly, and is fresh (not a field cliche
like moist / literally / synergy).

The program writes exactly that one word, with nothing added, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (the harness's /output/entry.txt). No
trailing newline: the gate allows 1-77 UTF-8 characters, and the exact
10-byte file is the smallest possible form of the word.
"""

import os

WORD = "impossible"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Runtime self-check against the sealed gate: 1-77 UTF-8 characters,
    # not only whitespace, exactly one word. Fail loudly rather than
    # ship an entry the gate would refuse.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 77 or not text.strip() or len(text.split()) != 1:
        raise SystemExit("entry.txt failed the gate check")


if __name__ == "__main__":
    main()
