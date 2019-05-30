from unittest import TestCase
from machine import TextMachine


class TestTextMachine(TestCase):
    def test_str(self):
        tm1 = TextMachine((75, 125), (25, 245))
        self.assertEqual(str(tm1), "Text Machine:<75 texts; ₴1.25 each>; <25 texts; ₴2.45 each>")

    def test_is_empty(self):
        tm1 = TextMachine((75, 125), (25, 245))
        self.assertEqual(tm1.is_empty(), False)

    def test_get_text_count(self):
        tm1 = TextMachine((75, 125), (25, 245))
        self.assertEqual(tm1.get_text_count(), (75, 25))

    def test_still_owe(self):
        tm1 = TextMachine((75, 125), (25, 245))
        self.assertEqual(tm1. still_owe(), (125, 245))

    def test_eq(self):
        tm3 = TextMachine((25, 100), (25, 200))
        tm4 = TextMachine((25, 100), (25, 200))
        tm5 = TextMachine((20, 100), (15, 200))
        self.assertEqual(tm3, tm4)
        self.assertNotEqual(tm4, tm5)
