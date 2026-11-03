import unittest
from diccionarios import *


class TestPromedio(unittest.TestCase):
    def test_unico(self):
        notas = [("juan", 8.0)]
        resultado_esperado = {"juan": 8.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)

    def test_varios_no_repetidos(self):
        notas = [("juan", 8.0),("jose",9.0),("sofia",10.0)]
        resultado_esperado = {"juan": 8.0,"jose": 9.0,"sofia": 10.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)

    def test_varios_repetidos(self):
        notas = [("juan", 8.0),("jose",9.0),("sofia",10.0),("jose", 7.0),("juan",9.0),("sofia",10.0),("luna",7.0)]
        resultado_esperado = {"juan": 8.5,"jose": 8.0,"sofia": 10.0, "luna": 7.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
