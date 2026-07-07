"""Core text statistics."""


def word_count(text: str) -> int:
    """Return the number of words in *text*.

    Words are separated by whitespace.
    """
    return len(text.split())


def unique_word_count(text: str) -> int:
    """Return the number of distinct words in *text*.

    Words are separated by whitespace and compared case-insensitively.
    """
    return len({word.casefold() for word in text.split()})


def average_word_length(text: str) -> float:
    """Return the average word length in *text*.

    Words are separated by whitespace.
    """
    words = text.split()
    if not words:
        return 0.0
    return sum(len(word) for word in words) / len(words)


def longest_word(text: str) -> str:
    """Return the longest word in *text*.

    Words are separated by whitespace.
    """
    return max(text.split(), key=len, default="")


def most_common_word(text: str) -> str:
    """Return the most frequent word in *text*.

    Words are separated by whitespace and compared case-insensitively.
    """
    counts: dict[str, int] = {}
    for word in text.split():
        normalized = word.casefold()
        counts[normalized] = counts.get(normalized, 0) + 1

    return max(counts, key=counts.get, default="")


def reading_time(text: str, wpm: int = 200) -> float:
    """Return the estimated reading time for *text* in minutes.

    Reading time is based on words per minute.
    """
    if wpm <= 0:
        raise ValueError("wpm must be greater than 0")
    return word_count(text) / wpm


def char_count(text: str, include_spaces: bool = False) -> int:
    """Return the number of characters in *text*.

    Whitespace is excluded unless *include_spaces* is true.
    """
    if include_spaces:
        return len(text)
    return len("".join(text.split()))


def sentence_count(text: str) -> int:
    """Return the number of sentences in *text*.

    Sentences end with '.', '!' or '?'.
    """
    if not text.strip():
        return 0
    count = 0
    in_terminator_run = False
    for ch in text:
        if ch in ".!?":
            if not in_terminator_run:
                count += 1
                in_terminator_run = True
        else:
            in_terminator_run = False
    return max(count, 1)


def paragraph_count(text: str) -> int:
    """Return the number of paragraphs in *text*.

    Paragraphs are separated by one or more blank lines.
    """
    count = 0
    in_paragraph = False
    for line in text.splitlines():
        if line.strip():
            if not in_paragraph:
                count += 1
                in_paragraph = True
        else:
            in_paragraph = False
    return count
