"""
Introducción a la Programación 
2do Cuatrimestre 2026
Práctica 7: Matrices
"""
import unittest
from clase11_141026 import *

"""
Tests Ordenados
"""
class Test_ordenados(unittest.TestCase):

    def test_1(self):
        lista = []
        self.assertTrue(ordenados(lista))

    def test_2(self):
        lista = [1,2,3]
        self.assertTrue(ordenados(lista))

    def test_3(self):
        lista = [3,2,1]
        self.assertFalse(ordenados(lista))


"""
Tests Sumar toda la matriz
"""
class Test_sumarTodaLaMatriz(unittest.TestCase):

    def test_1(self):
        matriz = []
        self.assertEqual(sumarTodaLaMatriz(matriz),0)


    def test_2(self):
        matriz = [[1,1,1],[1,1,1],[1,1,1]]
        self.assertEqual(sumarTodaLaMatriz(matriz),9)
    
    def test_3(self):
        matriz = [[1,-1],[-1,1]]
        self.assertEqual(sumarTodaLaMatriz(matriz),0)


"""
Test Columna
"""
# Test de columna
class Test_columna(unittest.TestCase):

    def test_1(self):
        matriz = [[1]]
        numero_columna = 0
        self.assertEqual(columna(matriz,numero_columna),[1])

    def test_2(self):
        matriz = [[1,2,3],[4,5,6]]
        numero_columna = 2
        self.assertEqual(columna(matriz,numero_columna),[3,6])
    
    def test_3(self):
        matriz = [[1,2,3],[4,5,6],[7,8,9]]
        numero_columna = 1
        self.assertEqual(columna(matriz,numero_columna),[2,5,8])

"""
Tests Columnas Ordenadas
"""
class Test_columnas_ordenadas(unittest.TestCase):   

    def test_1(self):
        matriz = [[1]]
        self.assertEqual(columnas_ordenadas(matriz),[True])

    def test_2(self):
        matriz = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(columnas_ordenadas(matriz),[True,True,True])
    
    def test_3(self):
        matriz = [[1,2,3],[2,5,2]]
        self.assertEqual(columnas_ordenadas(matriz),[True,False])




if __name__ == '__main__':
    unittest.main(verbosity=2)
