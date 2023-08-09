
import unittest

from translator import english_french, french_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_french(self):
        "Translate from English text to French"
        self.assertEqual(english_french('Hello'), 'Bonjour')
        self.assertEqual(english_french('Apple'), 'Pomme')
        self.assertNotEqual(english_french('Orange'), 'Salut')
        self.assertNotEqual(english_french('Hello'), 'Pomme')

class TestFrenchtoEnglish(unittest.TestCase):
    def test_french_english(self):
        "Translate from French text to English"
        self.assertEqual(french_english('Bonjour'), 'Hello')
        self.assertEqual(french_english('Pomme'), 'Apple')
        self.assertNotEqual(french_english('Salut'), 'Orange')
        self.assertNotEqual(french_english('Pomme'), 'Hello')

unittest.main()
