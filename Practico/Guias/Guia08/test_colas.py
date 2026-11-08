import unittest
from colas import *
from queue import Queue as Cola
from typing import TypeVar
T = TypeVar('T')

class test_cantidad_elementos(unittest.TestCase):
    def test_cantidad_ok(self):
        cola = Cola()
        cola.put(1)
        cola.put(2)
        cola.put(3)

        self.assertEqual(cantidad_elementos(cola),cola.qsize())

class test_intercalar(unittest.TestCase):
    def test_intercala_ok(self):
        c1 = Cola()
        c1.put(1)
        c1.put(2)
        c1.put(3)
        c2 = Cola()
        c2.put(5)
        c2.put(6)
        c2.put(7)

        resultado = intercalar(c1,c2)
        self.assertEqual(c1.qsize(),3)
        self.assertEqual(c2.qsize(),3)
        print('c1:')
        mostrar_cola(c1)
        print('c2:')
        mostrar_cola(c2)
        self.assertEqual(resultado.qsize(),6)
        print('resultado:\n')
        mostrar_cola(resultado)


class test_armar_secuencia_de_bingo(unittest.TestCase):
    def test_genera_ok(self):
        secuencia = armar_secuencia_de_bingo()
        self.assertEqual(secuencia.qsize(),100)

        lista_secuencia = []
        for i in range(0,100):
            numero = secuencia.get()
            lista_secuencia.append(numero)

        hay_repetido = False
        for i in range(0,100):
            if i < 99 and pertenece(lista_secuencia[i+1:len(lista_secuencia)-1],lista_secuencia[i]):
                hay_repetido = True

        self.assertFalse(hay_repetido)

if __name__ == '__main__':
    unittest.main(verbosity=2)
