"""
Introducción a la Programación 
2do Cuatrimestre 2026
Práctica 7: Matrices
"""
# Ordenados
def ordenados(s: list[int]) -> bool:
    i: int = 0
    while i < len(s)-1:
        if s[i] >= s[i+1]:
            return False
        i += 1

    return True

# Sumar toda la matriz
def sumarTodaLaMatriz(matriz: list[list[int]]) -> int:
    sumaMatriz: int = 0
    for fila in matriz:
        sumaMatriz += sumatoria(fila)
    return sumaMatriz

def sumatoria(terminos: list[int]) -> int:
    sumaTotal: int = 0
    for numero in terminos:
        sumaTotal += numero
    return sumaTotal

def sumarTodaLaMatriz2(matriz: list[list[int]]) -> int:
    sumaTotal: int = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            sumaTotal += matriz[i][j]
    return sumaTotal

# Columna
def columna(matriz: list[list[int]],j: int) -> list[int]:
    col: list[int] = []

    for fila in matriz:
        col.append(fila[j])

    return col

# Columnas ordenadas
def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    columnas_matriz: list[list[int]] = []
    for i in range(0,len(matriz[0])):
        columnas_matriz.append(columna(matriz,i))

    resultado: list[bool] = []
    for col in columnas_matriz:
        resultado.append(ordenados(col))

    return resultado