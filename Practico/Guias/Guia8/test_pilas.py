import unittest
import pilas
from queue import LifoQueue as Pila
from typing import TypeVar
T = TypeVar('T')

class test_generar_nros_al_azar(unittest.TestCase):
  def test_genera_pila_vacia(self):
    p: Pila[int] = pilas.generar_nros_al_azar(0,1,10)
    self.assertTrue(p.empty())
  
  def test_pila_respeta_cantidad(self):
    p: Pila[int] = pilas.generar_nros_al_azar(5,1,10)
    p_lista: list[int] = pilas.pila_a_lista(p)
    self.assertEqual(len(p_lista),5)

  def test_no_supera_maximo(self):
    p: Pila[int] = pilas.generar_nros_al_azar(5,1,10)
    p_lista: list[int] = pilas.pila_a_lista(p)
    
    maximo: int = p_lista[0]
    for i in p_lista:
      if i > maximo:
        maximo = i
    self.assertTrue(maximo <= 10)
  
  def test_no_tiene_numeros_debajo_del_minimo(self):
    p: Pila[int] = pilas.generar_nros_al_azar(5,1,10)
    p_lista: list[int] = pilas.pila_a_lista(p)

    minimo: int = p_lista[0]
    for i in p_lista:
      if i < minimo:
        minimo = i
    self.assertTrue(minimo >= 1)


class test_cantidad_elementos(unittest.TestCase):
  def test_no_tiene_elementos(self):
    p: Pila[int] = Pila()
    self.assertEqual(pilas.cantidad_elementos(p),0)

  def test_un_elemento(self):
    p: Pila[int] = Pila()
    p.put(1)
    self.assertEqual(pilas.cantidad_elementos(p),1)

  def test_varios_elementos(self):
    p: Pila[int] = Pila()
    p.put(1)
    p.put(10)
    p.put(5)
    p.put(7)
    p.put(3)
    self.assertEqual(pilas.cantidad_elementos(p),5)

if __name__ == '__main__':
  unittest.main(verbosity=2)
