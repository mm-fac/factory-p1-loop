"""Core text statistics."""


def word_count(text: str) -> int:
    """Return the number of words in *text*.

    Words are separated by whitespace.
    """
    return len(text.split())


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
    for ch in text:
        if ch in ".!?":
            count += 1
    return max(count, 1)
