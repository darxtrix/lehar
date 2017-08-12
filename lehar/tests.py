import unittest

from main import draw

class LeharMethodsTest(unittest.TestCase):

    def test_all_positives(self):
        self.assertEqual(draw([1,2,3,4,5]), '▂▄▅▇█')

    def test_some_negatives(self):
        self.assertEqual(draw([-1,2,-4,4]), '▃▆▁█')

    def test_missing_data(self):
        self.assertEqual(draw([1,'',2,'',4]),'▂ ▄ █')

    def test_input_as_strings(self):
        self.assertEqual(draw(['1','2','3','4','5']),'▂▄▅▇█')

    def test_color_option(self):
        self.assertEqual(draw(['1','2','3','4'],color='cyan'),'\x1b[36m▂▄▆█\x1b[0m')

    def test_max_zero(self):
        self.assertEqual(draw([-34,-12,-3,0]),'▁▆██')


if __name__ == '__main__':
    unittest.main()