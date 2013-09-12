#! /usr/bin/python
# -*- coding: utf-8 -*-
#run python -m chardetails.tests.chardetails_test from root directory
#of the repository
import unittest
from indicsyllabifier import getInstance


class TestIndicSyllabifier(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_info(self):
        self.assertIsInstance(self.instance.get_info(), str)

    def test_syllabify_english(self):
        self.assertEqual(self.instance.syllabify(u"A syllable is a unit of organization for a sequence of speech sounds."),
                         "A syl-lable is a u/nit of or-ga/ni/za/tion for se/qu_en-ce of speech sounds.")

    def test_syllabify_malayalam(self):
        self.assertEqual(self.instance.
                         syllabify(u"ഭാവിയെക്കുറിച്ചുള്ള കാഴ്ചപ്പാട്"),
                         [u'\u0d2d\u0d3e',
                          u'\u0d35\u0d3f',
                          u'\u0d2f\u0d46',
                          u'\u0d15\u0d4d\u0d15\u0d41',
                          u'\u0d31\u0d3f',
                          u'\u0d1a\u0d4d\u0d1a\u0d41',
                          u'\u0d33\u0d4d\u0d33',
                          u' ',
                          u'\u0d15\u0d3e',
                          u'\u0d34\u0d4d\u0d1a',
                          u'\u0d2a\u0d4d\u0d2a'])
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicSyllabifier)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
