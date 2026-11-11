from typing import TypeVar
T = TypeVar('T')

# Ej 1
def stock_productos(stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    lista_apariciones_producto: list[str] = []
    for elemento in stock_cambios:
        lista_apariciones_producto.append(elemento[0])

    lista_productos: list[str] = lista_sin_repetidos(lista_apariciones_producto)

    cambios_en_stock_dict: dict[str,list[int]] = {}
    for producto in lista_productos:
        cambios_en_stock_dict[producto] = []
        for actualizacion in stock_cambios:
            if actualizacion[0] == producto:
                cambios_en_stock_dict[producto].append(actualizacion[1])
    
    
    res: dict[str,tuple[int,int]] = {}
    for producto in cambios_en_stock_dict:
        res[producto] = (minimo_de_lista(cambios_en_stock_dict[producto]),maximo_de_lista(cambios_en_stock_dict[producto]))

    return res

def lista_sin_repetidos(lista: list[T]) -> list[T]:
    res: list[T] = []

    for elemento in lista:
        if elemento not in res:
            res.append(elemento)

    return res

def minimo_de_lista(lista: list[int]) -> int:
    minimo: int = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero

    return minimo

def maximo_de_lista(lista: list[int]) -> int:
    maximo: int = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero

    return maximo
