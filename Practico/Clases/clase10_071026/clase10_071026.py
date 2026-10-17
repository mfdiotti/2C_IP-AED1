# 1.3 Suma Total

def suma_total_v1(s: list[int]) -> int:
    suma: int = 0
    for i in s:
        suma += i
    return suma

def suma_total_v2(s: list[int]) -> int:
    suma: int = 0
    for i in range(0,len(s)):
        suma += s[i]
    return suma

def suma_total_v3(s: list[int]) -> int:
    suma: int = 0
    i: int = 0
    while i < len(s):
        suma += s[i]
        i += 1
    return suma

# Ejercicio actividad en papel

def palabras_unidas(ps: list[str]) -> str:
    res: str = ""
    for palabra in ps:
        if palabra != "" and res == "":
            res += palabra
        elif palabra != "":
            res += " " + palabra
    return res

def separada_por_comas(palabra: str) -> str:
    separada_comas: str = ""
    for letra in range(0,len(palabra)-1):
        separada_comas += palabra[letra] + ","
    separada_comas += palabra[len(palabra)-1]
    return separada_comas

def promedio(numeros: list[int]) -> int:
    return suma_total_v1(numeros) / len(numeros)

# 1.1 Pertenece

def pertenece1(s: list[int], e: int) -> bool:
    return e in s

def pertenece2(s: list[int], e: int) -> bool:
    if s == []:
        return False
    elif e == s[0]:
        return True
    else:
        return pertenece2(s[1:],e)

def pertenece3(s: list[int], e: int) -> bool:
    for i in s:
        if e == i:
            return True
    return False

#def pertenece4(s: list[int], e: int) -> bool:
#    index:int = 0
#    valorBool:bool = s[index] == e
#    while index < len(s):
#        valorBool = s[index] == e
#        index += 1
#    return valorBool

def pertenece5(s: list[int], e: int) -> bool:
    i = 0
    while i < len(s) and s[i] != e:
        i += 1

    return i < len(s)

# 2.1 cerosEnPosicionesPares1
def ceros_en_posiciones_pares1_v1(s: list[int]):
    for i in range(0,len(s)):
        if i % 2 == 0:
            s[i] = 0
        else:
            s[i] = s[i]

def ceros_en_posiciones_pares1_v2(s: list[int]):
    for i in range(0,len(s),2):
        s[i] = 0

