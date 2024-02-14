from palindromo import es_palindromo

# --- no le des bola a este código ---

import unittest


class Tests(unittest.TestCase):
    def test_palindromo(self):
        self.assertTrue(es_palindromo("aa"))
        self.assertTrue(es_palindromo("aaa"))
        self.assertTrue(es_palindromo("ababa"))
        self.assertTrue(es_palindromo("neuquen"))
        self.assertTrue(es_palindromo("121"))
        self.assertFalse(es_palindromo("21"))
        self.assertFalse(es_palindromo("as"))
        self.assertFalse(es_palindromo("ssa22sd"))
        self.assertFalse(es_palindromo("asdasdasddd"))
        self.assertFalse(es_palindromo("tu vieja"))


if __name__ == "__main__":
    unittest.main()
