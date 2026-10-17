import unittest
import clase10_071026

class test_sumaV1(unittest.TestCase):
    def test_listavacia(self):
        secuencia_vacia: list = []
        self.assertEqual(clase10_071026.suma_total_v1(secuencia_vacia), 0)
    
    def test_suma_0(self):
        secuencia_0: list = [0,0,0]
        self.assertEqual(clase10_071026.suma_total_v1(secuencia_0), 0)
    
    def test_suma_unelem(self):
        secuencia_1: list = [1]
        self.assertEqual(clase10_071026.suma_total_v1(secuencia_1), 1)

    def test_suma_hasta5(self):
        secuencia_5: list = [1,2,3,4,5]
        self.assertEqual(clase10_071026.suma_total_v1(secuencia_5), 15)

# Tests ejercicio actividad papel

    def test_PalabrasUnidas_1elem(self):
        secuencia_1: list = ["a"]
        self.assertEqual(clase10_071026.palabras_unidas(secuencia_1), "a")
    
    def test_PalabrasUnidas_mas_de_un_elem(self):
        secuencia_1: list = ["a","b","c"]
        self.assertEqual(clase10_071026.palabras_unidas(secuencia_1), "a b c")
    
    def test_PalabrasUnidas_elem_y_vacio(self):
        secuencia_1: list = ["a",""]
        self.assertEqual(clase10_071026.palabras_unidas(secuencia_1), "a")
