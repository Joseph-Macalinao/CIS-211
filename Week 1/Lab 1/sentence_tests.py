import unittest
import sentence


class T0_SentenceLength(unittest.TestCase):
    """Test the methods of the sentence class. Note that you can
       also create multiple test classes -- one per method."""

    def test_get_length_nonempty(self):
        """Check whether the length of a sentence is correct"""
        the_sentence_obj = sentence.Sentence('Hello world')
        self.assertEqual(the_sentence_obj.get_length(), 11)

    def test_get_length_empty(self):
        """Check whether the length of a sentence is correct"""
        the_sentence_obj = sentence.Sentence('')
        self.assertEqual(the_sentence_obj.get_length(), 0)


class T1_SentenceObject(unittest.TestCase):
    def test_build(self):
        sent = sentence.Sentence("Hello World!")
        self.assertEqual(sent.string, "Hello World!")

    def test_build_empty(self):
        sent = sentence.Sentence('')
        self.assertEqual(sent.string, '')


class T2_GetSentence(unittest.TestCase):

    def test_get_sentence(self):
        sent = sentence.Sentence("Hello World!")
        get = sent.get_sentence()
        self.assertEqual(get, "Hello World!")

    def test_get_empty(self):
        sent = sentence.Sentence('')
        get = sent.get_sentence()
        self.assertEqual(get, '')


class T3_GetWords(unittest.TestCase):

    def test_get_words(self):
        sent = sentence.Sentence("Hello World!")
        words = sent.get_words()
        self.assertEqual(words, ["Hello", "World!"])

    def test_get_words_empty(self):
        sent = sentence.Sentence('')
        words = sent.get_words()
        self.assertEqual(words, [])


class T4_GetLength(unittest.TestCase):

    def test_get_length(self):
        sent = sentence.Sentence("Hello World!")
        length = sent.get_length()
        self.assertEqual(length, 12)

    def test_get_length_empty(self):
        sent = sentence.Sentence('')
        length = sent.get_length()
        self.assertEqual(length, 0)


class T5_GetNumWords(unittest.TestCase):

    def test_get_num_words(self):
        sent = sentence.Sentence("Hello World!")
        num_words = sent.get_num_words()
        self.assertEqual(num_words, 2)

    def test_get_num_words_empty(self):
        sent = sentence.Sentence('')
        get_num_words = sent.get_num_words()
        self.assertEqual(get_num_words, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
