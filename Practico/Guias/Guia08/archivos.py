# Ej 19
# 19.1
def contar_lineas(nombre_archivo: str) -> int:
    
    archivo: TextIO = open(nombre_archivo, 'r')
    res: int = len(archivo.readlines())
    archivo.close()
    
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

