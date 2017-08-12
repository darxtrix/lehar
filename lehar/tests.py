# -*- coding: utf-8 -*-

import unittest

from main import draw

class LeharMethodsTest(unittest.TestCase):

    def test_all_positives(self):
        self.assertEqual(draw([1,2,3,4,5]), u'▂▄▅▇█')

    def test_some_negatives(self):
        self.assertEqual(draw([-1,2,-4,4]), u'▃▆▁█')

    def test_missing_data(self):
        self.assertEqual(draw([1,'',2,'',4]), u'▂ ▄ █')

    def test_input_as_strings(self):
        self.assertEqual(draw(['1','2','3','4','5']), u'▂▄▅▇█')

    def test_color_option(self):
        self.assertEqual(draw(['1','2','3','4'],color='cyan'), u'\x1b[36m▂▄▆█\x1b[0m')

    def test_max_zero(self):
        self.assertEqual(draw([-34,-12,-3,0]), u'▁▆██')

    def test_no_data_supplied(self):
        self.assertEqual(draw([]),u'')


if __name__ == '__main__':
    unittest.main()