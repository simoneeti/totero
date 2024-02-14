from palindromo import es_palindromo
from numeros_primos import es_numero_primo
from lista import numero_maximo

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
        self.assertTrue(es_numero_primo(89))
        self.assertTrue(es_numero_primo(67))
        self.assertTrue(es_numero_primo(43))
        self.assertTrue(es_numero_primo(31))
        self.assertTrue(es_numero_primo(167))
        self.assertFalse(es_numero_primo(10))
        self.assertFalse(es_numero_primo(12))
        self.assertFalse(es_numero_primo(32))
        self.assertFalse(es_numero_primo(25))
        self.assertFalse(es_numero_primo(55))

    def test_numeros_maximos(self):
        self.assertEqual(numero_maximo([0, 4, 87, 11, 22, 3]), 87)
        self.assertEqual(numero_maximo([978, 4, 87, 767, 22]), 978)
        self.assertEqual(numero_maximo([2202, 12000, 827, 50, 23, 443, 221]), 12000)
        self.assertEqual(numero_maximo([0, 2000, 87]), 2000)

    def test_ordenar_diccionario(self):
        pass


if __name__ == "__main__":
    unittest.main()
