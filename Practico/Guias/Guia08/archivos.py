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

# Ej 20
def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[int] = archivo.readlines()
    palabras: list[int] = lista_palabras(lineas)


    res: dict[int,int] = {}
    for palabra in palabras:
        longitud_palabra: int = len(palabra)

        if longitud_palabra in res.keys():
            res[longitud_palabra] += 1
        else:
            res[longitud_palabra] = 1

    archivo.close()

    return res

# Ej 21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    palabras: list[str] = lista_palabras(lineas)
    palabras_sin_repeticiones: list[str] = elimina_str_repetidos(palabras)
    palabra_por_cantidad: dict[str,int] = {}

    for palabra in palabras_sin_repeticiones:
        cantidad: int = 0
        for cadena in palabras:
            if cadena == palabra:
                cantidad += 1

        palabra_por_cantidad[palabra] = cantidad

    mas_frecuente: tuple[str,int] = (list(palabra_por_cantidad.keys())[0],palabra_por_cantidad[list(palabra_por_cantidad.keys())[0]])

    for palabra in palabra_por_cantidad.keys():
        if palabra_por_cantidad[palabra] > mas_frecuente[1]:
            mas_frecuente = (palabra,palabra_por_cantidad[palabra])

    archivo.close()

    return mas_frecuente[0]

def elimina_str_repetidos(l: list[str]) -> list[str]:
    res: list[str] = []

    for cadena in l:
        if cadena not in res:
            res.append(cadena)
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

# Ej 23
def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    archivo_entrada: TextIO = open(nombre_archivo_entrada,'r')
    lineas_archivo_entrada: list[str] = archivo_entrada.readlines()

    lineas_archivo_salida: list[int] = []

    for linea in lineas_archivo_entrada:
        lineas_archivo_salida.insert(0,linea)

    archivo_salida: TextIO = open(nombre_archivo_salida,'w')
    archivo_salida.writelines(lineas_archivo_salida)

    archivo_entrada.close()
    archivo_salida.close()

# Ej 24
def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    archivo: TextIO = open(nombre_archivo,'a')

    archivo.write(frase)

    archivo.close()

# Ej 25
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()

    lineas.insert(0,frase)

    archivo: TextIO = open(nombre_archivo,'w')
    archivo.writelines(lineas)
    archivo.close()


# Ej 26
def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    archivo = open(nombre_archivo,'rb')
    secuencia_bytes = archivo.read()
    archivo.close()

    res: list[str] = []
    cadena: str = ''
    for byte in secuencia_bytes:
        caracter = chr(byte)
        if es_caracter_legible(caracter):
            cadena += caracter
        else:
            if len(cadena) > 4:
                res.append(cadena)
            cadena = ''

    if len(cadena) > 4:
        res.append(cadena)

    return res

def es_caracter_legible(c: str) -> bool:
    es_letra_minus: bool = 'a' <= c and c <= 'z'
    es_letra_mayus: bool = 'A' <= c and c <= 'Z'
    es_letra: bool = es_letra_minus or es_letra_mayus
    es_numero: bool = '0' <= c and c < = '9'
    es_ascii: bool = es_letra or es_numero or c == '_' or c == ' '
    return es_ascii
