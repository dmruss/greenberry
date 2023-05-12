#
# parser tests
#

import unittest
import greenberry.utils.parse as parse


class GBParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.parser = parse.GreenBerryParse()
        return
    
    def test_simple_parse_print_one_word(self):
        words = ['print', 'a']
        self.parser.simple_parse(words=words, line=None)

    def test_simple_parse_print_eval(self):
        words = ['print', 'eval', '(2 + 3 - 4)']
        self.parser.simple_parse(words=words, line=None)

    def test_simple_parse_string(self):
        words = ['print', 'string', 'a', 'cat', 'walks', 'along', 'the', 'path']
        self.parser.simple_parse(words=words, line=None)

    def test_simple_parse_var_ref(self):
        # g_vars = {'words': ['x']}
        # words = ['var', 'x', '=', '1']
        # self.parser.simple_parse(g_vars, words)
       # TODO

    
        

if __name__ == "__main__":
    unittest.main(exit=False)