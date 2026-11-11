from queue import LifoQueue as Pila
from typing import TypeVar
T = TypeVar('T')
import random

# Ej 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for i in range(0,cantidad):
        numero_aleatorio: int = random.randint(desde,hasta)
        res.put(numero_aleatorio)

    return res

# Ej 2
def cantidad_elementos(p: Pila[T]) -> int:
    pila_temp: Pila[T] = Pila()
    cantidad: int = 0

    while not p.empty():
      pila_temp.put(p.get())
      cantidad += 1

    while not pila_temp.empty():
      p.put(pila_temp.get())

    return cantidad

# Ej 3
def buscar_el_maximo(p: Pila[int]) -> int:
    pila_temp: Pila[int] = Pila()
    maximo: int = p.get()

    pila_temp.put(maximo)
  
    while not p.empty():
      numero: int = p.get()
      if numero > maximo:
        maximo = numero
      pila_temp.put(numero)

    while not pila_temp.empty():
      p.put(pila_temp.get())

    return maximo

# Ej 4
def buscar_nota_maxima(p: Pila[tuple[str,int]]) -> tuple[str,int]:
    pila_temp: Pila[tuple[str,int]] = Pila()

    maxima_nota: tuple[str,int] = p.get()
    pila_temp.put(maxima_nota)

    maximo_numero: int = maxima_nota[1]

    while not p.empty():
        tupla_temp: tuple[str,int] = p.get()
        numero_tupla: int = tupla_temp[1]

        if numero_tupla > maximo_numero:
            maximo_numero = numero_tupla
            maxima_nota = tupla_temp

        pila_temp.put(tupla_temp)

    while not pila_temp.empty():
        p.put(pila_temp.get())
  
    return maxima_nota

# Ej 7
def intercalar(p1: Pila[T], p2: Pila[T]) -> Pila[T]:
    pila_temp: Pila[T] = Pila()
    p1_temp: Pila[T] = Pila()
    p2_temp: Pila[T] = Pila()

    while not p1.empty() and not p2.empty():
        elemento_p1: T = p1.get()
        elemento_p2: T = p2.get()

        pila_temp.put(elemento_p2)
        pila_temp.put(elemento_p1)
        p1_temp.put(elemento_p1)
        p2_temp.put(elemento_p2)

    while not p1_temp.empty():
        p1.put(p1_temp.get())

    while not p2_temp.empty():
        p2.put(p2_temp.get())

    res: Pila[T] = Pila()
    while not pila_temp.empty():
        res.put(pila_temp.get())

    return res

# Auxiliar para leer pilas
def pila_a_lista(p: Pila[T]) -> list[T]:
    pila_temp: Pila[T] = Pila()
    res: list[T] = []

    while not p.empty():
      ultimo_elemento: T = p.get()
      pila_temp.put(ultimo_elemento)
      res.append(ultimo_elemento)

    while not pila_temp.empty():
      p.put(pila_temp.get())

    return res
