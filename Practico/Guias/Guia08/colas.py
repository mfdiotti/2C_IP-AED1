from queue import Queue as Cola
import random
from typing import TypeVar
T = TypeVar('T')

# Ej 8
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    res: Cola[int] = Cola()

    for i in range(cantidad):
        numero_aleatorio: int = random.randint(desde,hasta)
        res.put(numero_aleatorio)

    return res

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

# Ej 10
def buscar_el_maximo(c: Cola[int]) -> int:
    cola_temp: Cola[int] = Cola()
    maximo: int = c.get()
    cola_temp.put(maximo)

    while not c.empty():
        numero: int = c.get()

        if numero > maximo:
            maximo = numero

        cola_temp.put(numero)

    while not cola_temp.empty():
        c.put(cola_temp.get())

    return maximo

# Ej 11
def buscar_nota_minima(c: Cola[tuple[str,int]]) -> tuple[str,int]:
    cola_temp: Cola[tuple[str,int]] = Cola()
    minima_nota: tuple[str,int] = c.get()
    cola_temp.put(minima_nota)

    while not c.empty():
        nota: tuple[str,int] = c.get()

        if nota[1] < minima_nota[1]:
            minima_nota = nota

        cola_temp.put(nota)

    while not cola_temp.empty():
        c.put(cola_temp.get())

    return minima_nota

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

# Ej 14
def pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
    cola_temp: Cola[T] = Cola()
    cantidad_urgentes: int = 0

    while not c.empty():
        paciente: tuple[int,str,str] = c.get()

        if paciente[0] < 4:
            cantidad_urgentes += 1

        cola_temp.put(paciente)

    while not cola_temp.empty():
        c.put(cola_temp.get())

    return cantidad_urgentes

# Ej 15
# 15.1
"""
propuesta 1:

problema atencion_a_clientes(in c: Cola(seq⟨Char⟩ x Z x Bool x Bool)) : Cola(seq⟨Char⟩ x Z x Bool x Bool) {
    requiere: {c no tiene elementos repetidos}
    requiere: {el primer componente de cada elemento en c no es vacio}
    asegura: {res es una permutacion de c}
    asegura: {para todo i, j, 0 ≤ i < j, e[i],e[j] ∈ c: (e[i][3] ∧ ¬e[j][3]) → pos(e[i],res) < pos(e[j],res)}
    asegura: {para todo i, j, 0 ≤ i < j, e[i],e[j] ∈ c: (¬e[i][3] ∧ e[i][2] ∧ ¬e[j][3] ∧ ¬e[j][2]) → pos(e[i],res) < pos(e[j],res)}
    asegura: {para todo i, j, 0 ≤ i < j, e[i],e[j] ∈ c: (e[i][2] = e[j][2] ∧ e[i][3] = e[j][3]) → pos(e[i],res) < pos(e[j],res) ↔ pos(e[i],c) < pos(e[j],c)}
}

aux:
p | q | ~p | ~q | p∧~q|
v   v    f    f    f
v   f    f    v    v
f   v    v    f    f
f   f    v    v    f

propuesta 2:

problema atencion_a_clientes(in c: Cola(seq⟨Char⟩ x Z x Bool x Bool)) : Cola(seq⟨Char⟩ x Z x Bool x Bool) {
    requiere: {c no tiene elementos repetidos}
    requiere: {el primer componente de cada elemento en c no es vacio}
    asegura: {res es una permutacion de c}
    asegura: {cada elemento de res posee un indice menor al siguiente (de existir) si:
        - Tiene prioridad ↔ elemento[3] ∧ True
        - Es cliente preferencial ↔ elemento[2] ∧ True
        - elemento[3] ∧ elemento[2] → posicion(elemento)@c < posicion(elemento)+1@c}
}
"""

# 15.2
def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    cola_temp: Cola[tuple[str,int,bool,bool]] = Cola()
    
    grupo_prioridad: Cola[tuple[str,int,bool,bool]] = Cola()
    grupo_preferencial: Cola[tuple[str,int,bool,bool]] = Cola()
    grupo_resto: Cola[tuple[str,int,bool,bool]] = Cola()

    while not c.empty():
        cliente: tuple[str,int,bool,bool] = c.get()
        cola_temp.put(cliente)

        if cliente[3]:
            grupo_prioridad.put(cliente)
        elif cliente[2]:
            grupo_preferencial.put(cliente)
        else:
            grupo_resto.put(cliente)

    res: Cola[tuple[str,int,bool,bool]] = Cola()
    while not grupo_prioridad.empty():
        res.put(grupo_prioridad.get())

    while not grupo_preferencial.empty():
        res.put(grupo_preferencial.get())

    while not grupo_resto.empty():
        res.put(grupo_resto.get())

    while not cola_temp.empty():
        c.put(cola_temp.get())

    return res

#auxiliares de cola
def cola_desde_lista(lista: list[T]) -> Cola[T]:
    cola: Cola[T] = Cola()
    for elemento in lista:
        cola.put(elemento)
    return cola

def mostrar_cola(c: Cola[T]) -> None:
    while not (c.empty()):
        print(c.get())
