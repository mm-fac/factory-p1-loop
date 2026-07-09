import pytest

from textstats import (
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


class TestUniqueWordCount:
    def test_repeats_differing_only_by_case_count_once(self):
        assert unique_word_count("The the THE quick") == 2

    def test_all_unique_text(self):
        assert unique_word_count("one two three") == 3

    def test_empty_string(self):
        assert unique_word_count("") == 0


class TestVocabularyRichness:
    def test_all_unique_text_returns_one(self):
        assert vocabulary_richness("one two three") == 1.0

    def test_repeated_words_returns_ratio(self):
        assert vocabulary_richness("the the quick fox") == 0.75

    def test_single_word(self):
        assert vocabulary_richness("hello") == 1.0

    def test_empty_string(self):
        assert vocabulary_richness("") == 0.0


class TestWordFrequencies:
    def test_counts_mixed_case_repeats_with_lowercase_keys(self):
        assert word_frequencies("The quick THE the") == {"the": 3, "quick": 1}

    def test_preserves_first_occurrence_order(self):
        frequencies = word_frequencies("Beta alpha ALPHA beta gamma")

        assert list(frequencies) == ["beta", "alpha", "gamma"]

    def test_empty_string(self):
        assert word_frequencies("") == {}

    def test_whitespace_only_string(self):
        assert word_frequencies("  \n\t  ") == {}


class TestTopWords:
    def test_returns_words_ordered_by_descending_count(self):
        assert top_words("red blue red green blue red") == ["red", "blue", "green"]

    def test_tie_returns_earliest_first_occurrence(self):
        assert top_words("beta alpha alpha beta gamma", n=2) == ["beta", "alpha"]

    def test_n_larger_than_vocabulary_returns_all_words(self):
        assert top_words("one two two", n=5) == ["two", "one"]

    def test_empty_string(self):
        assert top_words("") == []


class TestAverageSentenceLength:
    def test_multi_sentence_text(self):
        assert average_sentence_length("One two. Three four five!") == 2.5

    def test_single_sentence(self):
        assert average_sentence_length("One two three") == 3.0

    def test_empty_string(self):
        assert average_sentence_length("") == 0.0


class TestAverageWordLength:
    def test_returns_average_word_length(self):
        assert average_word_length("the quick brown fox") == 4.0

    def test_single_word(self):
        assert average_word_length("hello") == 5.0

    def test_empty_string(self):
        assert average_word_length("") == 0.0

    def test_whitespace_only_string(self):
        assert average_word_length("  \n\t  ") == 0.0


class TestMedianWordLength:
    def test_odd_count_returns_middle_length(self):
        assert median_word_length("a bb cccc") == 2.0

    def test_even_count_returns_mean_of_two_middle_lengths(self):
        assert median_word_length("a bb ccc dddd") == 2.5

    def test_single_word(self):
        assert median_word_length("hello") == 5.0

    def test_empty_string(self):
        assert median_word_length("") == 0.0

    def test_whitespace_only_string(self):
        assert median_word_length("  \n\t  ") == 0.0


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


class TestMostCommonWord:
    def test_returns_clear_winner(self):
        assert most_common_word("red blue red green") == "red"

    def test_counts_case_insensitively_and_returns_lowercase(self):
        assert most_common_word("The the THE quick") == "the"

    def test_tie_returns_earliest_first_occurrence(self):
        assert most_common_word("beta alpha alpha beta") == "beta"

    def test_empty_string(self):
        assert most_common_word("") == ""

    def test_whitespace_only_string(self):
        assert most_common_word("  \n\t  ") == ""


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


class TestLineCount:
    def test_multi_line_text_with_blank_lines_interspersed(self):
        text = "First line.\n\nSecond line.\n   \nThird line."

        assert line_count(text) == 3

    def test_single_line_without_trailing_newline(self):
        assert line_count("Only line.") == 1

    def test_whitespace_only_lines(self):
        assert line_count("   \n\t\n  ") == 0

    def test_empty_string(self):
        assert line_count("") == 0


class TestParagraphCount:
    def test_multi_paragraph_text(self):
        text = "First paragraph.\nStill first.\n\nSecond paragraph."

        assert paragraph_count(text) == 2

    def test_multiple_consecutive_blank_lines_separate_paragraphs(self):
        text = "First paragraph.\n\n   \n\t\nSecond paragraph."

        assert paragraph_count(text) == 2

    def test_single_paragraph(self):
        assert paragraph_count("One paragraph.\nStill the same paragraph.") == 1

    def test_leading_and_trailing_blank_lines_are_ignored(self):
        text = "\n  \nOnly paragraph.\n\n"

        assert paragraph_count(text) == 1

    def test_empty_string(self):
        assert paragraph_count("") == 0

    def test_whitespace_only_string(self):
        assert paragraph_count("  \n\t  ") == 0


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

        expected = {
            "word_count": 3,
            "char_count": 15,
            "sentence_count": 2,
            "reading_time": 0.015,
        }
        assert result.returncode == 0
        assert result.stderr == ""
        assert result.stdout == json.dumps(expected) + "\n"
        assert json.loads(result.stdout) == expected

    def test_pretty_prints_indented_json_matching_compact(self, tmp_path):
        import json
        import subprocess
        import sys

        text_file = tmp_path / "sample.txt"
        text_file.write_text("Hello world. Bye!", encoding="utf-8")

        compact = subprocess.run(
            [sys.executable, "-m", "textstats", str(text_file)],
            check=False,
            capture_output=True,
            text=True,
        )
        pretty = subprocess.run(
            [sys.executable, "-m", "textstats", "--pretty", str(text_file)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert pretty.returncode == 0
        assert pretty.stderr == ""
        assert json.loads(pretty.stdout) == json.loads(compact.stdout)
        assert pretty.stdout == json.dumps(json.loads(compact.stdout), indent=2) + "\n"

    def test_pretty_flag_may_follow_file_argument(self, tmp_path):
        import json
        import subprocess
        import sys

        text_file = tmp_path / "sample.txt"
        text_file.write_text("Hello world. Bye!", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "-m", "textstats", str(text_file), "--pretty"],
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

    def test_unknown_argument_exits_with_usage_error(self, tmp_path):
        import subprocess
        import sys

        text_file = tmp_path / "sample.txt"
        text_file.write_text("Hello world.", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "-m", "textstats", "--unknown", str(text_file)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 1
        assert result.stdout == ""
        assert result.stderr == "usage: python -m textstats [--pretty] <file>\n"

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
