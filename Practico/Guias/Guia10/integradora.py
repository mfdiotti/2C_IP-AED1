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

# Ej 2
def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []

    for codigo in codigos_barra:
        if es_primo(codigo % 1000):
            res.append(codigo)

    return res

def es_primo(entero: int) -> bool:
    cantidad_divisores: int = 0
    for i in range(1,entero+1):
        if entero % i == 0:
            cantidad_divisores += 1

    return cantidad_divisores == 2

# Ej 3
def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    pacientes_buscados: list[str] = ['perro','gato']
    inicio_actual: int = 0
    longitud_actual: int = 0

    inicio_subsecuencia_maxima: int = 0
    longitud_maxima_subsecuencia: int = 0

    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] in pacientes_buscados:
            if longitud_actual == 0:
                inicio_actual = i

            longitud_actual += 1

            if longitud_actual > longitud_maxima_subsecuencia:
                inicio_subsecuencia_maxima = inicio_actual
                longitud_maxima_subsecuencia = longitud_actual
        else:
            longitud_actual = 0

    return inicio_subsecuencia_maxima

# Ej 4
def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
    horarios_fila_por_dia: list[list[str]] = transpuesta(grilla_horaria)

    res: list[tuple[bool,bool]] = []

    for dia in horarios_fila_por_dia:
        turnos_dia: tuple[bool,bool] = (turno_m(dia),turno_n(dia))
        res.append(turnos_dia)

    return res

def transpuesta(matriz: list[list[T]]) -> list[list[T]]:
    res: list[list[T]] = []

    for i in matriz:
        res.append(columna(matriz,i))

    return res

def columna(matriz: list[list[T]], columna: int) -> list[T]:
    res: list[T] = []

    for fila in matriz:
        res.append(fila[columna])

    return res

def turno_m(dia: list[T]) -> bool:
    i: int = 0
    while i < 3:
        if dia[i] != dia[i+1]:
            return False

    return True

def turno_n(dia: list[T]) -> bool:
    i: int = 3
    while i < 7:
        if dia[i] != dia[i+1]:
            return False

    return True
