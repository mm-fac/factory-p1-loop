# factory-p1-loop

**Sacrificial P1 validation repo for the Mac mini AI factory.**

This repo exists to prove one thing end-to-end: **issue → `@codex` PR → required checks → merge, fully autonomous** (architecture v6.4.1, §10 P1). It contains a deliberately small Python library (`textstats`) with real tests so the loop exercises real work, not no-ops.

- Work arrives as GitHub Issues.
- Codex cloud picks up issues and opens PRs on `codex/*` branches.
- The `ci` check (ruff + pytest) is required on `main`.
- PRs from `codex/*` branches (or labeled `automerge`) get GitHub auto-merge enabled and land on green — no human in the loop.

Nothing here is production. The repo is disposable by design; delete it when P1 exits.

## Local dev

```sh
pip install pytest ruff
ruff check .
pytest -q
```

## Library usage

Import public helpers directly from `textstats`:

```python
from textstats import word_count

print(word_count("small loops, real checks"))
```

### Public functions

#### `average_word_length(text: str) -> float`

Return the average word length in `text`.

```python
from textstats import average_word_length

average_word_length("small loops")
# 5.0
```

#### `char_count(text: str, include_spaces: bool = False) -> int`

Return the number of characters in `text`, excluding whitespace unless `include_spaces` is true.

```python
from textstats import char_count

char_count("small loops")
# 10
char_count("small loops", include_spaces=True)
# 11
```

#### `line_count(text: str) -> int`

Return the number of non-blank lines in `text`.

```python
from textstats import line_count

line_count("one\n\ntwo\n")
# 2
```

#### `longest_word(text: str) -> str`

Return the longest word in `text`.

```python
from textstats import longest_word

longest_word("tiny validation repository")
# 'validation'
```

#### `most_common_word(text: str) -> str`

Return the most frequent word in `text`, compared case-insensitively.

```python
from textstats import most_common_word

most_common_word("CI ci tests")
# 'ci'
```

#### `paragraph_count(text: str) -> int`

Return the number of paragraphs in `text`, separated by one or more blank lines.

```python
from textstats import paragraph_count

paragraph_count("first paragraph\n\nsecond paragraph")
# 2
```

#### `reading_time(text: str, wpm: int = 200) -> float`

Return the estimated reading time for `text` in minutes, based on words per minute.

```python
from textstats import reading_time

reading_time("one two three four", wpm=2)
# 2.0
```

#### `sentence_count(text: str) -> int`

Return the number of sentences in `text`; sentences end with `.`, `!`, or `?`.

```python
from textstats import sentence_count

sentence_count("Ready? Ship it!")
# 2
```

#### `unique_word_count(text: str) -> int`

Return the number of distinct words in `text`, compared case-insensitively.

```python
from textstats import unique_word_count

unique_word_count("Loop loop checks")
# 2
```

#### `word_count(text: str) -> int`

Return the number of whitespace-separated words in `text`.

```python
from textstats import word_count

word_count("small loops, real checks")
# 4
```

## Command line

Run the CLI with `python -m textstats [--pretty] <file>` to print JSON statistics for a text file.

- `<file>`: path to the text file to analyze.
- `--pretty`: pretty-print the JSON output with two-space indentation.

Example invocation:

```sh
python -m textstats --pretty sample.txt
```

Example JSON output:

```json
{
  "word_count": 4,
  "char_count": 21,
  "sentence_count": 1,
  "reading_time": 0.02
}
```
