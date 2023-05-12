#
# parser tests
#

import unittest
import greenberry.utils.parse as parse


class GBParserTests(unittest.TestCase):
    def test_simple_parse(self):
        g_vars = {'words': 'a'}
        words = ['print', 'a b c', 'b', 'c']
        line = None
        parser = parse.GreenBerryParse()
        parser.simple_parse(words, line)



if __name__ == "__main__":
    unittest.main(exit=False)