"""textstats — tiny text statistics library."""

__version__ = "0.1.0"

from textstats.stats import (
    average_sentence_length,
    average_word_length,
    char_count,
    line_count,
    longest_word,
    median_word_length,
    most_common_word,
    paragraph_count,
    reading_time,
    sentence_count,
    top_words,
    unique_word_count,
    vocabulary_richness,
    word_count,
    word_frequencies,
)

__all__ = [
    "__version__",
    "average_sentence_length",
    "average_word_length",
    "char_count",
    "line_count",
    "longest_word",
    "median_word_length",
    "most_common_word",
    "paragraph_count",
    "reading_time",
    "sentence_count",
    "top_words",
    "unique_word_count",
    "vocabulary_richness",
    "word_count",
    "word_frequencies",
]
