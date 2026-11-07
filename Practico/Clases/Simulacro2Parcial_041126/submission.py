from queue import LifoQueue as Pila


# Ejercicio 1
def ejercicio1(s: list[int], n: int) -> list[int]:
    lista_temp_pares_que_suman: list[tuple[int]] = []
    
    i: int = 0
    while i < len(s)-1:
        if s[i] + s[i+1] == n:
            par_suma_n: tuple[int] = (s[i],s[i+1])
            lista_temp_pares_que_suman.append(par_suma_n)
        i += 1

    indice_maximo: int = 0

    i: int = 0
    while i < len(lista_temp_pares_que_suman)-1:
        if lista_temp_pares_que_suman[i][0] > lista_temp_pares_que_suman[i+1][0]:
            indice_maximo = lista_temp_pares_que_suman[i][0]
        else:
            indice_maximo = lista_temp_pares_que_suman[i+1][0]
        i += 1

    for tupla in lista_temp_pares_que_suman:
        if tupla[0] == indice_maximo:
            res: list[int] = [tupla[0],tupla[1]]

    return res

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
    lista_candidatos: list[str] = list(eleccion1.values()) + list(eleccion2.values())

    cant_votos_conservados_por_candidato_temp: dict[str,int] = {}

    for candidato in lista_candidatos:
        cant_votos_conservados_por_candidato_temp[candidato] = 0
    
    for ciudadano in lista_ciudadanos:
        if eleccion1[ciudadano] == eleccion2[ciudadano]:
            cant_votos_conservados_por_candidato_temp[candidato] += 1
        else:
            cant_votos_conservados_por_candidato_temp[candidato] += 0

    res: dict[str,int] = {}
    for candidato in list(cant_votos_conservados_por_candidato_temp.keys()):
        if cant_votos_conservados_por_candidato_temp[candidato] != 0:
            res[candidato] = cant_votos_conservados_por_candidato_temp[candidato]

    return res