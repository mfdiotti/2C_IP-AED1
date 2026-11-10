from queue import LifoQueue as Pila


# Ejercicio 1
def ejercicio1(s: list[int], n: int) -> list[int]:
    res: list[int] = []

    i: int = 0
    while i < len(s):
        sucesion_temporal: list[int] = []
        j: int = i

        while j < len(s) and sumatoria(sucesion_temporal) < n:

            sucesion_temporal.append(s[j])

            if sumatoria(sucesion_temporal) == n:
                res.clear()
                for numero in sucesion_temporal:
                    res.append(numero)
            j += 1

        i += 1

    return res

def sumatoria(sucesion: list[int]) -> int:
    sumatoria: int = 0

    for numero in sucesion:
        sumatoria += numero

    return sumatoria

# Ejercicio 2
def ejercicio2(examenes: Pila[(str, int)]) -> Pila[str]:
    #lista_examenes: list[tuple[str,int]] = pila_a_lista(examenes)
    res: Pila[str] = Pila()

    lista_temp_tema1: list[str] = []
    lista_temp_tema2: list[(str,int)] = []
    #pila_temp: Pila[(str,int)] = Pila()
    while not examenes.empty():
        examen: tuple[str,int] = examenes.get()
        if examen[1] == 1:
            lista_temp_tema1.insert(0,examen[0])
        elif examen[1] == 2:
            lista_temp_tema2.insert(0,examen)

    for examen in lista_temp_tema2:
        examenes.put(examen)

    for nombre in lista_temp_tema1:
        res.put(nombre)

    return res

def pila_a_lista(pila: Pila[(str,int)]) -> list[(str,int)]:
    lista: list[(str,int)] = []
    while not pila.empty():
        lista.insert(0,pila.get())

    for elemento in lista:
        pila.put(elemento)

    return lista

# Ejercicio 3
def ejercicio3(A: list[list[int]]) -> None:
    for fila in A:
        minimo_de_fila: int = minimo_de_lista(fila)
        fila.append(minimo_de_fila)


def minimo_de_lista(lista: list[int]) -> int:
    minimo: int = lista[0]
    i: int = 0
    while i < len(lista):
        if lista[i] < minimo:
            minimo = lista[i]
        i += 1

    return minimo


# Ejercicio 4
def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str]) -> dict[str, int]:
    lista_ciudadanos: list[str] = list(eleccion1.keys())
    lista_candidatos: list[str] = list(eleccion1.values())

    cant_votos_conservados_por_candidato_temp: dict[str,int] = {}

    for candidato in lista_candidatos:
        cant_votos_conservados_por_candidato_temp[candidato] = 0

    for ciudadano in lista_ciudadanos:
        if eleccion1[ciudadano] == eleccion2[ciudadano]:
            candidato = eleccion1[ciudadano]
            cant_votos_conservados_por_candidato_temp[candidato] += 1

    res: dict[str,int] = {}
    for candidato in cant_votos_conservados_por_candidato_temp:
        if cant_votos_conservados_por_candidato_temp[candidato] != 0:
            res[candidato] = cant_votos_conservados_por_candidato_temp[candidato]

    return res
