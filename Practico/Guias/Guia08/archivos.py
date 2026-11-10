from typing import TextIO

# Ej 19
# 19.1
def contar_lineas(nombre_archivo: str) -> int:
    
    archivo: TextIO = open(nombre_archivo, 'r')
    res: int = len(archivo.readlines())
    archivo.close()
    
    return res

# 19.2
def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        if palabra in linea:
            return True

    archivo.close()
    return False

# 19.3
def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    palabras: list[str] = lista_palabras(lineas)
    cantidad_aparciones: int = 0

    for p in palabras:
        if p == palabra:
            cantidad_aparciones += 1

    archivo.close()
    return cantidad_aparciones

def lista_palabras(lineas: list[str]) -> list[str]:
# Usa funciones str.isalpha() y lower(), no permitidas en parcial.
    palabras: list[int] = []

    palabra: str = ''

    for linea in lineas:
        for caracter in linea:
            if caracter.isalpha():
                palabra += caracter.lower()
            elif not caracter.isalpha() and len(palabra) > 0:
                palabras.append(palabra)
                palabra = ''

    return palabras

def es_caracter_alfabetico(cadena: str) -> bool:
# Alternativa a str.isalpha() (no contempla tildes, ni otro tipo de acentuacion)
    letras: str = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'

    if len(cadena) < 1:
        return False

    for caracter in cadena:
        if caracter not in letras:
            return False

    return True

def mayuscula_a_minuscula(cadena: str) -> str:
# Alternativa a str.lower() (no contempla tildes, ni otro tipo de acentuacion)
    mayusculas: str = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minusculas: str = 'abcdefghijklmnñopqrstuvwxyz'

    res: str = ''

    for caracter in cadena:
        if caracter in mayusculas:
            posicion_letra: int = mayusculas.index(caracter)
            res += minusculas[posicion_letra]
        else:
            res += caracter

    return res

# Ej 22
def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    archivo_entrada: TextIO = open(nombre_archivo_entrada,'r')

    lineas_archivo_entrada = archivo_entrada.readlines()

    lineas_sin_comentarios = []

    for linea in lineas_archivo_entrada:
        if not es_comentario(linea) and linea != '\n':
            lineas_sin_comentarios.append(linea)

    archivo_salida = open(nombre_archivo_salida,'w')

    archivo_salida.writelines(lineas_sin_comentarios)
    
    archivo_entrada.close()
    archivo_salida.close()

def es_comentario(linea: str) -> bool:
    i: int = 0
    primer_caracter: str = linea[0]
    while primer_caracter == ' ' and i < (len(linea)-1):
        i += 1
        primer_caracter = linea[i]

    return primer_caracter == '#'

