import pytest

from textstats import (
    average_word_length,
    char_count,
    longest_word,
    reading_time,
    sentence_count,
    word_count,
)


class TestWordCount:
    def test_simple_sentence(self):
        assert word_count("the quick brown fox") == 4

    def test_single_word(self):
        assert word_count("hello") == 1

    def test_empty_string(self):
        assert word_count("") == 0

    def test_multiple_spaces_do_not_create_words(self):
        assert word_count("a  b") == 2

    def test_newlines_separate_words(self):
        assert word_count("a\nb") == 2

    def test_leading_whitespace_is_ignored(self):
        assert word_count("  lead") == 1

    def test_tabs_separate_words(self):
        assert word_count("a\tb") == 2

    def test_whitespace_only_string(self):
        assert word_count("  \n\t  ") == 0


class TestAverageWordLength:
    def test_returns_average_word_length(self):
        assert average_word_length("the quick brown fox") == 4.0

    def test_single_word(self):
        assert average_word_length("hello") == 5.0

    def test_empty_string(self):
        assert average_word_length("") == 0.0

    def test_whitespace_only_string(self):
        assert average_word_length("  \n\t  ") == 0.0


class TestLongestWord:
    def test_returns_longest_word(self):
        assert longest_word("the quick brown fox") == "quick"

    def test_tie_returns_first_longest_word(self):
        assert longest_word("one two six") == "one"

    def test_single_word(self):
        assert longest_word("hello") == "hello"

    def test_empty_string(self):
        assert longest_word("") == ""

    def test_whitespace_only_string(self):
        assert longest_word("  \n\t  ") == ""


class TestReadingTime:
    def test_estimates_minutes_from_word_count(self):
        assert reading_time("word " * 100) == 0.5

    def test_uses_custom_words_per_minute(self):
        assert reading_time("one two three", wpm=60) == 0.05

    def test_empty_string(self):
        assert reading_time("") == 0.0

    def test_whitespace_only_string(self):
        assert reading_time("  \n\t  ") == 0.0

    def test_non_positive_wpm_raises_value_error(self):
        with pytest.raises(ValueError):
            reading_time("words", wpm=0)

    def test_negative_wpm_raises_value_error(self):
        with pytest.raises(ValueError):
            reading_time("words", wpm=-1)


class TestCharCount:
    def test_excludes_spaces_by_default(self):
        assert char_count("a b c") == 3

    def test_includes_spaces_when_asked(self):
        assert char_count("a b c", include_spaces=True) == 5

    def test_empty_string(self):
        assert char_count("") == 0


class TestSentenceCount:
    def test_single_sentence(self):
        assert sentence_count("Hello there.") == 1

    def test_multiple_sentences(self):
        assert sentence_count("One. Two! Three?") == 3

    def test_ellipsis_counts_as_one_boundary(self):
        assert sentence_count("Wait... What?!") == 2

    def test_question_exclamation_run_counts_as_one_boundary(self):
        assert sentence_count("Really?! Yes.") == 2

    def test_no_terminator_counts_as_one(self):
        assert sentence_count("no punctuation here") == 1

    def test_empty_string(self):
        assert sentence_count("") == 0


class TestCli:
    def test_prints_stats_as_json(self, tmp_path):
        import json
        import subprocess
        import sys

        text_file = tmp_path / "sample.txt"
        text_file.write_text("Hello world. Bye!", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "-m", "textstats", str(text_file)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert result.stderr == ""
        assert json.loads(result.stdout) == {
            "word_count": 3,
            "char_count": 15,
            "sentence_count": 2,
            "reading_time": 0.015,
        }

    def test_missing_file_exits_with_error(self, tmp_path):
        import subprocess
        import sys

        missing_file = tmp_path / "missing.txt"

        result = subprocess.run(
            [sys.executable, "-m", "textstats", str(missing_file)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 1
        assert result.stdout == ""
        assert "error: could not read" in result.stderr
        assert str(missing_file) in result.stderr
