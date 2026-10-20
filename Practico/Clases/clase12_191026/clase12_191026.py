from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from typing import TypeVar
 
T = TypeVar('T')

# Ejercicio 1.1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]: 
    res: Pila[int] = Pila()
    for _ in range(0,cantidad):
        numero: int = random.randint(desde,hasta) 
        res.put(numero)
    return res

#auxiliares de pila
def pila_desde_lista (lista: list[T]) -> Pila[T]:
    res: Pila[T] = Pila()
    for e in lista:
        res.put(e)
    return res

pila_desde_lista([1,2,3,4])

def mostrar_pila (p: Pila[T]) -> None:
    pila_temp: Pila[T] = Pila()

    while not (p.empty()):
        e: T = p.get()
        print(e)
        pila_temp.put(e)

    while not (pila_temp.empty()):
        e: T = pila_temp.get()
        p.put(e)

# Ejercicio 1.3
def buscar_el_maximo(p: Pila[int]) -> int:
    pila_temp: Pila[int] = Pila()
    maximo: int = p.get()
    pila_temp.put(maximo)
    while not (p.empty()):
        num: int = p.get()
        if num > maximo:
            maximo = num
        pila_temp.put(num)
    while not(pila_temp.empty()):
        e: int = pila_temp.get()
        p.put(e)
    return maximo

    
# Ejercicio 2.13.1
def armarSecuencideBingo() -> Cola[int]:
    lista: list[int] = list(range(0,100))

    random.shuffle(lista)

    cola: Cola[int] = Cola()
    for i in lista:
        cola.put(i)

    return cola

# Ejercicio 2.13.2
def pertenece (cadena: list[T], elem:T) -> bool:
    for elemento in cadena:
        if elem == elemento:
            return True
    return False
    
def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
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

carton = [1,4]
#bolillero = cola_desde_lista([0,1,2,3,4])
#mostrar_cola(bolillero)
#jugarCartonDeBingo(carton,bolillero)





#auxiliares de cola
def cola_desde_lista (lista: list[T]) -> Cola[T]:
    cola: Cola[T] = Cola()
    for elemento in lista:
        cola.put(elemento)
    return cola

def mostrar_cola (c: Cola[T]) -> None:
    while not (c.empty()):
        print(c.get())
