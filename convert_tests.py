import unittest
from convert import str_to_float
class ConvertTests(unittest.TestCase):

    def test_str_to_float(self):
        input = "-125.2"
        expected = -125.2
        actual = str_to_float(input)
        self.assertEqual(expected,actual)

    def test_str_to_float(self):
        input = ".-125.2"
        expected = None
        actual = str_to_float(input)
        self.assertEqual(expected,actual)