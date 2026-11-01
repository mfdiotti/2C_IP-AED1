import unittest
import clase12_191026
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import TypeVar
 
T = TypeVar('T')

class test_generar_nros_al_azar(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_genera_vacia(self):
        p: Pila[int] = clase12_191026.generar_nros_al_azar(0,0,10)
        self.assertEqual(p.empty(),True)

class test_buscar_el_maximo(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_1(self):
        pila: Pila[int] = Pila()
        pila_copia: Pila[int] = Pila()
        pila.put(10)
        pila.put(1)
        pila.put(5)
        pila.put(3)
        pila_copia.put(10)
        pila_copia.put(1)
        pila_copia.put(5)
        pila_copia.put(3)
        maximo = clase12_191026.buscar_el_maximo(pila)
        self.assertEqual(maximo, 10)
        #No funciona, hay que recorrer ambas pilas para verificar que son iguales. pila y pila_copia son iguales a su pos en memoria.
        #self.assertEqual(pila,pila_copia)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
