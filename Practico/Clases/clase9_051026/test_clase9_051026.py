import unittest
import clase9_051026

#Ejemplo de test con dos casos, uno devuelve faliure, el otro no
class test1(unittest.TestCase):
    def test_1(self):
        self.assertTrue(True)
    def test_2(self):
        self.assertTrue(False)

#Test para cuenta_regresiva_solo_pares_y_es_par
class cuenta_regresiva_solo_pares_y_es_par_test(unittest.TestCase):
    def test_desde_par(self):
        self.assertTrue(clase10.cuenta_regresiva_solo_pares_y_es_par(10))
    def test_desde_impar(self):
        self.assertFalse(clase10.cuenta_regresiva_solo_pares_y_es_par(11))

#Ejecuta los tests cuando se ejecuta el archivo en terminal
#if __name__ == '__main__':
#    unittest.main(verbosity=2)
