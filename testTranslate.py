"""module to test translate.py module"""
import translate, unittest

class test_english_to_french(unittest.TestCase):
    def test1(self):
        """Method to test translate from english to french"""
        self.assertEqual(translate.english_to_french("hello"), "bonjour")
        self.assertNotEqual(translate.english_to_french("goodbye"), "bonjour")

class test_french_to_english(unittest.TestCase):
    def test1(self):
        """Method to test translate from french to english"""
        self.assertEqual(translate.french_to_english("bonjour"), "hello")
        self.assertNotEqual(translate.french_to_english("bonjour mon ami"), "hello my enemy")

unittest.main()
