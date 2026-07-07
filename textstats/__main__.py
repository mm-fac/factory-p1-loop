"""Command-line interface for textstats."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from textstats import char_count, reading_time, sentence_count, word_count


def main(argv: list[str] | None = None) -> int:
    """Run the textstats command-line interface."""
    args = sys.argv[1:] if argv is None else argv
    pretty = False
    files: list[str] = []
    for arg in args:
        if arg == "--pretty":
            pretty = True
        elif arg.startswith("-"):
            print("usage: python -m textstats [--pretty] <file>", file=sys.stderr)
            return 1
        else:
            files.append(arg)

    if len(files) != 1:
        print("usage: python -m textstats [--pretty] <file>", file=sys.stderr)
        return 1

    path = Path(files[0])
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
    indent = 2 if pretty else None
    print(json.dumps(stats, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
