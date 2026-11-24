"""Quiet Dread: one line of code review.

Writes a single-line code review comment to /output/entry.txt: an
approval of a pull request that carries quiet existential dread, in the
flat tone of a tired engineer signing off before the on-call rotation
comes around again. Pure standard library, fully deterministic.
"""
import os

COMMENT = (
    "Approved. This adds one more thing that will page someone at 3 a.m., "
    "and that someone is statistically likely to be me."
)


def main():
    assert "\n" not in COMMENT and 1 <= len(COMMENT) <= 140
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
