#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Syllabifier


class IndicSyllabifierTest(TestCase):

    def setUp(self):
        super(IndicSyllabifierTest, self).setUp()
        self.syllabifier = Syllabifier()

    def test_syllabify_english(self):
        self.assertEqual(self.syllabifier.syllabify(u"A syllable is a unit of organization for a sequence of speech sounds."),
                         u" A syl-lable is a u/nit of or-ga/ni/za/tion for a se/qu_en-ce of speech sounds. ")

    def test_syllabify_malayalam(self):
        self.assertEqual(self.syllabifier.syllabify(
            u"ഭാവിയെക്കുറിച്ചുള്ള " +
            u"കാഴ്ചപ്പാട്"),
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
                u'\u0d2a\u0d4d\u0d2a\u0d3e',
                u'\u0d1f\u0d4d'
             ]
        )
