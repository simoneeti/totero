from palindromo import es_palindromo
from numeros_primos import es_numero_primo

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

    def test_numeros_primos(self):
        self.assertTrue(89)
        self.assertTrue(67)
        self.assertTrue(43)
        self.assertTrue(31)
        self.assertTrue(167)
        self.assertFalse(10)
        self.assertFalse(12)
        self.assertFalse(32)
        self.assertFalse(25)
        self.assertFalse(55)


if __name__ == "__main__":
    unittest.main()
