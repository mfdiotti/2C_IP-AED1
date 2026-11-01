import numpy as np

# Parte 1 - Recorrido y busqueda en secuencias

# Ejercicio 1

# 1.1
def perteneceV1(s: list[int], e: int) -> bool:
  for i in s:
    if i == e:
      return True
  return False

def perteneceV2(s: list[int], e: int) -> bool:
  return e in s

def perteneceV3(s: list[int], e: int) -> bool:
  i: int = 0
  while i < len(s) and s[i] !=e:
    i += 1
  return i < len(s)

# 1.2
def divide_a_todosV1(s: list[int], e: int) -> bool:
  cantMultiplos: int = 0
  for i in s:
    if i % e == 0:
      cantMultiplos += 1
    else:
      cantMultiplos += 0
  return cantMultiplos == len(s)

def divide_a_todosV2(s: list[int], e: int) -> bool:
  i: int = 0
  while i < len(s):
    if (s[i] % e) != 0:
      break
    i += 1
  return i == len(s)

def divide_a_todosV3(s: list[int], e: int) -> bool:
  for i in s:
    if i % e != 0:
      return False
  return True

# 1.3
def suma_total(s: list[int]) -> int:
  res: int = 0
  for i in s:
    res += i
  return res

# 1.4
def maximo(s: list[int]) -> int:
  if s == []:
    pass
  lista_mayor_al_principio: list[int] = []
  for numero in s:
    if lista_mayor_al_principio == []:
      lista_mayor_al_principio.insert(0,numero)
    elif numero >= lista_mayor_al_principio[0]:
      lista_mayor_al_principio.insert(0,numero)
    else:
      lista_mayor_al_principio.insert(1,numero)
  return lista_mayor_al_principio[0]

# 1.5
def minimo(s: list[int]) -> int:
  lista_menor_al_principio: list[int] = []
  for numero in s:
    if lista_menor_al_principio == []:
      lista_menor_al_principio.insert(0,numero)
    elif numero <= lista_menor_al_principio[0]:
      lista_menor_al_principio.insert(0,numero)
    else:
      lista_menor_al_principio.insert(1,numero)
  return lista_menor_al_principio[0]

# 1.6
def ordenados1(s: list[int]) -> bool:
  if s == []:
    return False

  i: int = 0
  while i < (len(s)-1):
    if s[i] > s[i+1]:
      return False
    i += 1
  
  return True

def ordenados2(s: list[int]) -> bool:
  i: int = 0
  lista_mayor_a_menor: list[int] = []
  s_reducida: list[int] = s.copy()
  while i < len(s):
    if s_reducida == []:
      return lista_mayor_a_menor
    else:
      maximo_local = maximo(s_reducida)
      lista_mayor_a_menor.insert(0,maximo_local)
      s_reducida.remove(maximo_local)
    i += 1
  return lista_mayor_a_menor == s

# 1.7
def pos_maximo(s: list[int]) -> int:
  if s == []:
    return -1
  return s.index(maximo(s))

# 1.8
def pos_minimo(s: list[int]) -> int:
  if s == []:
    return -1
  
  s2: list[int] = s.copy()
  s2 = reverso_lista(s2)
  return len(s2) - (s2.index(minimo(s2)) + 1)

def reverso_lista(lista: list) -> list: # Funcion auxiliar dado que list.reverse() no esta permitida.
  lista_reverso: list = []
  for elemento in lista:
    lista_reverso.insert(0,elemento)
  return lista_reverso

# 1.9 
def long_mayor_a_siete(s: list[str]) -> bool:
  for palabra in s:
    if len(palabra) > 7:
      return True
  return False

# 1.10
def es_palindroma(s: str) -> bool:
  if s == '' or len(s) == 1:
    return True

  palabra_lista: list[str] = []
  
  for letra in s:
    palabra_lista.append(letra)

  palabra_reverso: list[str] = reverso_lista(palabra_lista)
  
  return palabra_lista == palabra_reverso

# 1.11
def iguales_consecutivos(s: list[int]) -> bool:
  i: int = 0
  while i < (len(s)-2):
    if s[i] == s[i+1] and s[i+1] == s[i+2]:
      return True
    i += 1

  return False

# 1.12
def vocales_distintas(s: str) -> bool:
  letras_palabra: list[str] = []
  for letra in s:
    letras_palabra.append(letra)

  vocales: list[str] = ['a','e','i','o','u']

  vocales_palabra: list[str] = []
  for letra in letras_palabra:
    if letra in vocales:
      vocales_palabra.append(letra)

  vocales_palabra: list[str] = quita_repetidos(vocales_palabra)

  return len(vocales_palabra) >= 3

def quita_repetidos(lista: list) -> list:
  # Auxiliar, recibe una lista y devuelve la misma lista sin las primeras apariciones de cualquier elemento que este mas de una vez.
  lista_sin_repetidos: list = lista.copy()
  for elemento in lista_sin_repetidos:
    if lista_sin_repetidos.count(elemento) > 1:
      lista_sin_repetidos.remove(elemento)

  return lista_sin_repetidos

# 1.13
def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
  pass

# 1.14
def cantidad_digitos_impares(s: list[int]) -> int:
  digitos_totales: list[str] = []
  for i in s:
    numero_como_string: str = str(i)
    for caracter in numero_como_string:
      digitos_totales.append(int(caracter))

  digitos_impares: list[int] = []
  for numero in digitos_totales:
    if (numero % 2) != 0:
      digitos_impares.append(numero)
  
  return len(digitos_impares)

# Parte 2 - Recorrido: filtrando, modificando y procesando secuencias

# Ejercicio 2

# 2.1
def ceros_en_posiciones_pares(s: list[int]):
  i: int = 0
  while i < len(s):
    if s.index(s[i]) % 2 == 0:
      s.pop(i)
      s.insert(i,0)
    i += 1

# 2.2
def ceros_en_posiciones_pares2(s: list[int]) -> list[int]:
  res: list[int] = s.copy()
  ceros_en_posiciones_pares(res)
  return res

# 2.3
def sin_vocales1(s: str) -> str: # Usando listas
  vocales = ['a','e','i','o','u']
  letras_palabra: list[str] = []
  for letra in s:
    letras_palabra.append(letra)

  for letra in letras_palabra:
    if letra in vocales:
      letras_palabra.remove(letra)

  palabra_sin_vocales: str = ''.join(letras_palabra) # str.join() no permitido en parcial

  return palabra_sin_vocales

def sin_vocales2(s: str) -> str: # Usando strings
  vocales: str = 'aeiou'
  palabra_sin_vocales: str = ''

  for letra in s:
    if letra not in vocales:
      palabra_sin_vocales += letra

  return palabra_sin_vocales

# 2.4
def reemplaza_vocales(s: str) -> str:
  vocales: str = 'aeiou'
  reemplazo_palabra: str = ''

  for letra in s:
    if letra in vocales:
      reemplazo_palabra += '-'
    else:
      reemplazo_palabra += letra

  return reemplazo_palabra

# 2.5
def da_vuelta_str(s: str) -> str:
  letras_palabra: list[str] = []
  for letra in s:
    letras_palabra.insert(0,letra)

  palabra_reverso: str = ''
  for letra in letras_palabra:
    palabra_reverso += letra

  return palabra_reverso

# 2.6
def eliminar_repetidos(s: str) -> str:
  letras_palabra: list[str] = []
  for letra in s:
    letras_palabra.append(letra)

  sin_repetidos_list: list[str] = quita_repetidos(letras_palabra)

  sin_repetidos_str: str = ''
  for letra in sin_repetidos_list:
    sin_repetidos_str += letra

  return sin_repetidos_str

# Ejercicio 3
def resultado_materia(notas: list[int]) -> int:
  promedio: int = suma_total(notas) // len(notas)
  nota_minima: int = minimo(notas)
  res: int = 0

  if nota_minima >= 4 and promedio >= 7:
    res += 1
  elif nota_minima >=4 and promedio >=4:
    res += 2
  elif nota_minima < 4 or promedio < 4:
    res += 3

  return res

# Ejercicio 4
def saldo_actual(movimientos: list[tuple[str,int]]) -> int:
  saldo: int = 0

  for movimiento in movimientos:
    if movimiento[0] == 'I':
      saldo += movimiento[1]
    elif movimiento[0] == 'R':
      saldo += movimiento[1]

  return saldo

# Parte 3 - Matrices
"""
Nota: defino fila de matriz como lista perteneciente a una secuencia de listas.
Ej, m = [[1,2,3],[1,2,3]] es una matriz ∈ R^{2x3} (dos filas, tres columnas).
"""
# Ejercicio 5

# 5.1
def pertenece_a_cada_uno_version1(s: list[list[int]], e: int, res: list[bool]):
  for lista in s:
    res.append(perteneceV1(lista,e))

# 5.2
def pertenece_a_cada_uno_version2(s: list[list[int]], e: int, res: list[bool]):
  res.clear()
  
  for lista in s:
    res.append(perteneceV1(lista,e))

# 5.3
def pertenece_a_cada_uno_version3(s: list[list[int]], e: int) -> list[bool]:
  res: list[bool] = []
  
  for lista in s:
    res.append(perteneceV1(lista,e))

  return res

# 5.4
"""
La primer diferencia entre las tres especificaciones reside en el tipo de pasaje de parametro. En la primera y segunda version,
los procedimientos reciben tres parametros: dos de entrada y uno de salida. Al ser procedimientos, no retornan un resultado
sino que modifican el parametro de salida. En cambio, la tercer version es una funcion, toma dos parametros de entrada
y devuelve un resultado.
La segunda diferencia esta en el primer asegura de cada especificacion: mientras en version1 asegura {|res| ≥ |s|}, tanto version2
como version3 tienen como asegura {|res| = |s|}.
Para pensar en terminos de relacion de fuerza, observando que la diferencia entre las especificaciones de version1 y version2 esta
en el primer asegura (version1 asegura: {|res| ≥ |s|}, version2 asegura: {|res| = |s|}), si tomamos:
 - p = (|res| = |s|) = asegura v2,
 - q = (|res| > |s|)
 - (p ∨ q) = (|res| ≥ |s|) = asegura v1
proposiciones, es posible verificar su tabla de verdad.
Tomando P = asegura v1, Q = asegura v2. Recordar que A "es mas fuerte que" B si A → B es tautologia.

| p=(|res| = |s|) | q=(|res| > |s|) | P = asegura v1 | Q = asegura v2 | P → Q | Q → P |
|-----------------|-----------------|----------------|----------------|-------|-------|
|         V       |        V        |        V       |        V       |   F   |   V   |
|         V       |        F        |        V       |        V       |   V   |   V   |
|         F       |        V        |        V       |        F       |   F   |   V   |  Nota: Se toma el ≥ como un ∨ (or) inclusivo.
|         F       |        F        |        F       |        F       |   V   |   V   |        Si p: x=y, q: x>y → p∨q: x≥y

Concuimos que Q → P es tautologia, por ende el asegura de la version2 es mas fuerte que el asegura de version1.
En terminos de la implementacion en python, la implementacion de version2 verifica los asegura de version1, ya que |res|=|s| V → |res|≥|s| V.
En cambio, el caso contrario no es posible ya que |res|≥|s| V !→ |res|=|s| V.
"""

# Ejercicio 6

# 6.1
def es_matriz(s: list[list[int]]) -> bool:
  if s == [] or s[0] == []:
    return False

  i: int = 0
  while i < len(s)-1:
    if len(s[i]) != len(s[i+1]):
      return False
    i += 1

  return True

# 6.2
def filas_ordenadas(m: list[list[int]], res: list[bool]) :
  res.clear()

  for fila in m:
    res.append(ordenados1(fila))

# 6.3
def columna(m: list[list[int]], c: int) -> list[int]:
  columna: list[int] = []
  for fila in m:
    columna.append(fila[c])

  return columna

# 6.4
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
  lista_de_columnas: list[list[int]] = []
  for indice in range(0,len(m)):
    lista_de_columnas.append(columna(m,indice))

  resultado: list[bool] = []
  for col in lista_de_columnas:
    resultado.append(ordenados1(col))

  return resultado

# 6.5
def transponer(m: list[list[int]]) -> list[list[int]]:
  transpuesta: list[list[int]] = []
  for indice in range(0,len(m)):
    transpuesta.append(columna(m,indice))

  return transpuesta

# 6.6
def quien_gana_tateti(m: list[list[str]]) -> int:
  gana_O: list[str] = ['O','O','O']
  gana_X: list[str] = ['X','X','X']
  ganador: int = 0
  
  filas_columnas_y_diagonales: list[list[str]] = m + transponer(m) + [diagonales_matriz(m,'P')] + [diagonales_matriz(m,'S')]
  
  if gana_O in filas_columnas_y_diagonales:
    ganador += 0
  elif gana_X in filas_columnas_y_diagonales:
    ganador += 1
  else:
    ganador += 2
  
  return ganador

def diagonales_matriz(m: list[list], d: str) -> list:
  # Devuelve la diagonal principal o secundaria segun d='P' o d='S'
  diagonal: list = []
  rango = range(0,len(m))
  for i in rango:
    if d == 'P':
      diagonal.append(m[i][i])
    elif d == 'S':
      diagonal.append(m[i][(len(m)-1)-rango.index(i)])

  return diagonal

# 6.7
#def exponenciacion_matriz(d: int, p: int) -> list[list[int]]:
#  m = np.random.randint(10,size=(d,d))
#  columnas: list[list[int]] = transpuesta(m)
#  
#  for fila in m:
#    for columna in columnas:
#      

# Parte 4 - Programas interactivos usando secuencias.

# Ejercicio 7

# 7.1
def lista_estudiantes() -> list[str]:
  estudiantes: list[str] = []

  estudiante: str = 'Inicio'
  finaliza: list[str] = ['listo','']
  
  while estudiante.lower() not in finaliza:
    estudiante = input('Ingrese el nombre del estudiante.\nFinaliza cuando ingresa "listo" o presiona ENTER sin ingresar nada: ')
    if estudiante.lower() not in finaliza:
      estudiantes.append(estudiante)

  return estudiantes

# 7.2
def historial_monedero() -> list[tuple[str,int]]:
  historial: list[tuple[str,int]] = []
  usuario: str = input('Ingrese\n"C" para cargar creditos\n"D" para descontar\n"X" para finalizar: ')
  monto: int = 0
  saldo: int = 0

  while usuario.upper() != 'X':
    if usuario.upper() == 'C':
      monto = input('Ingrese el monto a cargar: ')
      historial.append(('Carga',int(monto)))
    elif usuario.upper() == 'D':
      monto = input('Ingrese el monto a descontar: ')
      historial.append(('Descuento',- int(monto)))
    
    usuario: str = input('Ingrese\n"C" para cargar creditos\n"D" para descontar\n"X" para finalizar: ')

  for operacion in historial:
    saldo += operacion[1]

  return historial#, f'El saldo actual es {saldo}'

# 7.3
def siete_y_medio() -> str:
  cartas_obtenidas: list[int] = []
  usuario: str = input('Siete y medio\nTomo una carta: T\nMe planto: X')
  suma_cartas: float = 0
  
  while usuario.lower() != 'x':
    carta: int = np.random.randint(1,12)

    if carta not in [8,9]:
      cartas_obtenidas.append(carta)
      print(f'Tomaste la carta {carta}')
      if carta in range(1,10):
        suma_cartas += carta
      elif carta in range(10,13):
        suma_cartas += 0.5
    else:
      carta: int = np.random.randint(1,12)
      

    if suma_cartas > 7.5:
      print(f'Perdiste, tus cartas suman {suma_cartas}, pasaste los siete y medio.')
    else:
      usuario: str = input('Tomas otra carta?\nTomo una carta: T\nMe planto: X')

  print(f'Tus cartas fueron {cartas_obtenidas}')
