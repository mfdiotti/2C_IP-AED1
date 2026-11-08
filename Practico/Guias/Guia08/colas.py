from queue import Queue as Cola
import random
from typing import TypeVar
T = TypeVar('T')

# Ej 9
def cantidad_elementos(c: Cola[T]) -> int:
    cola_temp: Cola[T] = Cola()
    cantidad: int = 0

    while not c.empty():
        elemento: T = c.get()
        cola_temp.put(elemento)
        cantidad += 1

    while not cola_temp.empty():
        c.put(cola_temp.get())

    return cantidad

# Ej 12
def intercalar(c1: Cola[T], c2: Cola[T]) -> Cola[T]:
    res: Cola[T] = Cola()
    c1_temp: Cola[T] = Cola()
    c2_temp: Cola[T] = Cola()

    while not c1.empty() and not c2.empty():
        elemento_c1: T = c1.get()
        elemento_c2: T = c2.get()

        res.put(elemento_c1)
        res.put(elemento_c2)
        c1_temp.put(elemento_c1)
        c2_temp.put(elemento_c2)

    while not c1_temp.empty():
        c1.put(c1_temp.get())

    while not c2_temp.empty():
        c2.put(c2_temp.get())

    return res

# Ej 13
# 13.1
def armar_secuencia_de_bingo() -> Cola[int]:
    lista: list[int] = list(range(0,100))

    random.shuffle(lista)

    cola: Cola[int] = Cola()
    for i in lista:
        cola.put(i)

    return cola


def pertenece(cadena: list[T], elem:T) -> bool:
    for elemento in cadena:
        if elem == elemento:
            return True
    return False


# 13.2
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    carton_sin_salir: list[int] = carton.copy()
    veces: int = 0
    bolillero_temp: Cola[int] = Cola()
    while len(carton_sin_salir) > 0:
        num_bolillero: int = bolillero.get()
        bolillero_temp.put(num_bolillero)
        if num_bolillero in carton_sin_salir:
            carton_sin_salir.remove(num_bolillero)
        veces += 1

    while not bolillero.empty():
        bolillero_temp.put(bolillero.get())

    while not bolillero_temp.empty():
        bolillero.put(bolillero_temp.get())

    return veces


#auxiliares de cola
def cola_desde_lista(lista: list[T]) -> Cola[T]:
    cola: Cola[T] = Cola()
    for elemento in lista:
        cola.put(elemento)
    return cola

def mostrar_cola(c: Cola[T]) -> None:
    while not (c.empty()):
        print(c.get())
