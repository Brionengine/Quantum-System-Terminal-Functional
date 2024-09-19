import unittest
from nlp_engine.nlp_processor import NLPEngine

class TestNLPEngine(unittest.TestCase):
    def test_parse_input(self):
        nlp_engine = NLPEngine()
        result = nlp_engine.parse_input("List all files in the current directory")
        self.assertIn("ls", result)

if __name__ == '__main__':
    unittest.main()
