"""Command-line interface for textstats."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from textstats import char_count, reading_time, sentence_count, word_count


def main(argv: list[str] | None = None) -> int:
    """Run the textstats command-line interface."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python -m textstats <file>", file=sys.stderr)
        return 1

    path = Path(args[0])
    try:
        text = path.read_text()
    except OSError as exc:
        print(f"error: could not read {path}: {exc.strerror}", file=sys.stderr)
        return 1

    stats = {
        "word_count": word_count(text),
        "char_count": char_count(text),
        "sentence_count": sentence_count(text),
        "reading_time": reading_time(text),
    }
    print(json.dumps(stats))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
