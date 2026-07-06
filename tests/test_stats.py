from textstats import char_count, sentence_count, word_count


class TestWordCount:
    def test_simple_sentence(self):
        assert word_count("the quick brown fox") == 4

    def test_single_word(self):
        assert word_count("hello") == 1

    def test_empty_string(self):
        assert word_count("") == 0


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

    def test_no_terminator_counts_as_one(self):
        assert sentence_count("no punctuation here") == 1

    def test_empty_string(self):
        assert sentence_count("") == 0
