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

  
