import math

# Ejericio 1 - Definir las funciones y procedimientos.
# 1.1 - 
"""
problema perimetro() : R {
  requiere: { True }
  asegura: { res = 2 * π }
}
"""
def imprimir_hola_mundo():
  print(hola_mundo)

hola_mundo = '¡Hola Mundo!'

# 1.2 - imprimir_un_verso(): que imprima un verso de una cancion que vos elijas, respetando los saltos de linea mediante el caracter \n.
def imprimir_un_verso():
  verso = estrofasCancion[14]
  print(f'\n{verso}\n')

# 1.2 (alternativa)
def imprimir_un_versoV2(x: int):
  if x > 14:
    x = x % 10
  else:
    x = x
  estrofa = f'{estrofasCancion[x]}\n{estrofasCancion[x+1]}'
  print(estrofa)

estrofasCancion = [
'Slip inside the eye of your mind',
'Don\'t you know you might find',
'A better place to play?',
'You said that you\'d never been',
'But all the things that you\'ve seen',
'Will slowly fade away',
'So I start a revolution from my bed',
'\'Cause you said the brains I had went to my head',
'Step outside, summertime\'s in bloom',
'Stand up beside the fireplace',
'Take that look from off your face',
'You ain\'t ever gonna burn my heart out',
'And so, Sally can wait',
'She knows it\'s too late as we\'re walkin\' on by',
'Her soul slides away',
'\"But don\'t look back in anger,\" I heard you say'] #Oasis - Don't Look Back In Anger

# 1.3 - raizDe2(): que devuelva la raiz cuadrada de 2 con 4 decimales. Ver funcion round
def raizDe2():
  raizDe2 = round(math.sqrt(2), 4)
  return raizDe2

# 1.4 - factorial_de_dos()
"""
problema factorial_2() : Z {
  requiere:{ True }
  asegura: { res=2! }
}
"""
def factorial_de_dos():
  factorialDeDos = math.factorial(2)
  return factorialDeDos

#  1.5 - perimetro: que devuelva el perimetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando import math y la constante math.pi
"""
problema perimetro() : R {
  requiere: { True }
  asegura: { res = 2 * π }
}
"""
def perimetro():
  perimetroRadio1 = 2 * math.pi
  return perimetroRadio1

#Ejercicio 2 - Definir las funciones y procedimientos con parametros.
# 2.1
"""
problema imprimir_saludo( in nombre: String ) {
  requiere: { True }
  asegura: { imprime "Hola < nombre >" por pantalla }
}
"""
def imprimir_saludo(nombre: str):
  print(f'Hola {nombre}')

# 2.2 - raiz_cuadrada_de(numero): que devuelva la raiz cuadrada del numero
def raiz_cuadrada_de(numero: int) -> float:
  raizCuadrada = math.sqrt(numero)
  return raizCuadrada

# 2.3
def fahrenheit_a_celsius(temp_far: int) -> float:
  celsius = ((temp_far - 32) * 5) / 9
  return celsius

# 2.4
def imprimir_dos_veces():
  estribilloDoble = 2 * estribillo
  print(estribilloDoble)

estribillo = f'{estrofasCancion[12]}\n{estrofasCancion[13]}\n{estrofasCancion[14]}\n{estrofasCancion[15]}\n'

# 2.5
def es_multiplo_de(n: int, m: int) -> bool:
  #si el resto de dividir n sobre m es 0, n es multiplo de m
  k = n % m
  return bool(k==0)

# 2.6
def es_par(numero: int) -> bool:
  return es_multiplo_de(numero, 2)

# 2.7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
  cantidad_de_pizzas = math.ceil((comensales * min_cant_de_porciones) / 8)
  return cantidad_de_pizzas

# Ejercicio 3 - Resolver utilizando los operadores logicos and, or, not. Resolver sin utilizar alternativa condicional if.
# 3.1
def alguno_es_0(numero1: float, numero2: float) -> bool:
  valorBool = (numero1 == 0) or (numero2 == 0)
  return valorBool

# 3.2
def ambos_son_0(numero1: float, numero2: float) -> bool:
  valorBool = (numero1 == 0) and (numero2 == 0)
  return valorBool

# 3.3
def es_nombre_largo(nombre: str) -> bool:
  esLargo = (len(nombre)>=3) and (len(nombre)<=8)
  return esLargo

# 3.4
def es_bisiesto(yr: int) -> bool:
  esBisiesto = es_multiplo_de(yr,400) or (es_multiplo_de(yr,4) and (not es_multiplo_de(yr,100)))
  return esBisiesto


# Ejercicio 4
"""
Usando composicion de funciones (como en funcional). Resolver este ejercicio usando las funciones min y max.

En una plantación de pinos, de cada árbol se conoce la altura expresada en metros. El peso de un pino se puede estimar a partir de la
altura de la siguiente manera:
- 3 kg por cada centímetro hasta 3 metros,
- 2 kg por cada centímetro arriba de los 3 metros.
Por ejemplo:
- 2 metros pesan 600 kg, porque 200 * 3 = 600
- 5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.
Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino fuera de este
rango no le sirve a la fábrica.
Definir las siguientes funciones, deducir qué parámetros tendrán a partir del enunciado. Se pueden usar funciones auxiliares si fuese
necesario para aumentar la legibilidad.
"""
# 4.1 - Definir la función peso_pino
def peso_pino(metrosPino: int) -> int:
  if metrosPino > 3:
    pesoPino = 900 + (metrosPino*100 - 300) * 2
  else:
    pesoPino = metrosPino*100 * 3
  return pesoPino

# 4.2 - Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
def es_peso_util(pesoPino: int) -> bool:
  pesoUtil = max(pesoPino,400) == pesoPino and min(pesoPino, 1000) == pesoPino
  return pesoUtil

# 4.3 - Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
def sirve_pino(metrosPino: int) -> str:
  if metrosPino > 3:
    pesoPino = 900 + (metrosPino*100 - 300) * 2
  else:
    pesoPino = metrosPino*100 * 3
  
  pesoUtil = max(pesoPino,400) == pesoPino and min(pesoPino, 1000) == pesoPino
  
  if pesoUtil:
    mensaje = 'El pino sirve'
  else:
    mensaje = 'El pino no sirve'

  print(mensaje)

# 4.4 - Definir sirve_pino usando composición de funciones.
def sirve_pinoV2(metrosPino: int) -> str:
  if es_peso_util(peso_pino(metrosPino)):
    mensaje = 'El pino sirve'
  else:
    mensaje = 'El pino no sirve'
  print(mensaje)

# Ejercicio 5
"""
Implementar los siguientes problemas de alternativa condicional (if/else). Los enunciados pueden no ser del todo claros,
especificar los problemas en nuestro lenguaje de especificacion y programar en base a tu propuesta de especificaion.
"""
# 5.1
"""
doble_si_es_par(numero): que devuelve el doble del numero en caso de ser par y el mismo numero en caso contrario.

Especificacion propuesta:

problema doble_si_es_par ( in numero: Integer ) : Integer {
  requiere: { numero ∈ R }
  asegura: { res = 2 * numero ∧ numero es multiplo de 2 }
  asegura: { res = numero ∧ numero no es multiplo de 2 }
}
"""
def doble_si_es_par(numero: int) -> int:
  if es_multiplo_de(numero, 2):
    res = numero * 2
  else:
    res = numero
  return res

# 5.2
"""
devolver_valor_si_es_par_si_no_el_que_sigue(numero): devuelve el mismo numero si es par, y si no, el siguiente.
Analizar distintas formas de implementacion (usando un if-then-else y dos if). ¿Todas Funcionan?

Especificacion propuesta:

problema devolver_valor_si_es_par_si_no_el_que_sigue ( in numero: Integer ) : Integer {
  requiere: { numero ∈ Z }
  asegura: { res = numero ∧ numero es multiplo de 2 }
  asegura: { res = numero + 1 ∧ numero no es multiplo de 2}
}
"""
def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int) -> int: # Version if-then-else
  if es_multiplo_de(numero, 2):
    res = numero
  else:
    res = numero + 1
  return res

def devolver_valor_si_es_par_si_no_el_que_sigueV2(numero: int) -> int: # Version "dos if"
  if es_multiplo_de(numero, 2):
    res = numero
  if not(es_multiplo_de(numero, 2)):
    res = numero + 1
  return res

# 5.3
"""
doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero): en otro caso, devolver el numero original.
Analizar distintas formas de implementacion (usando un if-then-else, dos if o alguna opcion de operacion logica).
¿Todas funcionan? ¿Cual es el resultado si la entrada es 18?

Especificacion propuesta;

problema doble_si_es_multiplo3_el_triple_si_es_multiplo9 ( in numero: Integer ) : Integer {
  requiere: { numero ∈ Z }
  asegura: { res = 2 * numero ∧ numero es multiplo de 3 y no es multiplo de 9 }
  asegura: { res = 3 * numero ∧ numero es multiplo de 9 y no es multiplo de 3 }
  asegura: { res = numero ∧ numero no es multiplo de 3 }
  asegura: { res = numero ∧ numero no es multiplo de 9 }
}
"""
# Si la especificaion contempla el caso: numero es multiplo de ambos, entonces devuelve numero sin modificar el valor.
def doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int: # Version if-then-else con operaciones logicas
  if es_multiplo_de(numero,3) and not(es_multiplo_de(numero,9)):
    numero *= 2
  elif es_multiplo_de(numero,9) and not(es_multiplo_de(numero,3)):
    numero *= 3
  elif es_multiplo_de(numero,3) and es_multiplo_de(numero,9):
    numero = numero
  else:
    numero =  numero
  return numero

# 5.4
"""
lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga 
"Tu nombre tiene muchas letras!" y si no, "Tu nombre tiene menos de 5 caracteres"

Especificacion propuesta:

problema lindo_nombre ( in nombre: String) : String {
  requiere: { |nombre| > 0 }
  asegura: { (res = "Tu nombre tiene muchas letras!") ↔ ( |nombre| >= 5 ) }
  asegura: { (res = "Tu nombre tiene menos de 5 caracteres") ↔ ( |nombre| < 5 ) }
}
"""
def lindo_nombre(nombre: str) -> str:
  if len(nombre) > 4:
    print('Tu nombre tiene muchas letras!')
  else:
    print('Tu nombre tiene menos de 5 caracteres')

# 5.5 
"""
elRango(numero) que imprime por pantalla "Menor a 5" si el numero es menor a 5, "Entre 10 y 20" si el numero esta en ese rango
y "Mayor a 20" si el numero es mayor a 20.

Especificacion propuesta:

problema elRango ( in numero: Floating ) : String {
  requiere: { numero ∈ R }
  asegura: { (res = "Menor a 5") ↔ (numero < 5) }
  asegura: { (res = "Entre 10 y 20") ↔ (10 <= numero <= 20) }
  asegura: { (res = "Mayor a 20") ↔ (numero > 20 )}
}
"""
def elRango(numero: float) -> str:
  if numero < 5:
    print('Menor a 5')
  elif numero >= 10 and numero <= 20:
    print('Entre 10 y 20')
  elif numero > 20:
    print('Mayor a 20')

# 5.6
"""
En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan a los 63 años.
Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de las personas se les ordena ir
a trabajar. Implemente una funcion que, dados los parametros de sexo (F o M) y edad, imprima la frase que corresponda segun el
caso: "Anda de vacaciones" o "Te toca trabajar"

Especificacion propuesta:

problema clasifica_edad_sexo( in sexo: Char, in edad: Integer ) : String {
  requiere: { sexo = 'F' ∨ sexo = 'M' }
  requiere: { edad > 0 }
  asegura: { (res = "Anda de vacaciones") ↔ (edad < 18) }
  asegura: { (res = "Anda de vacaciones") ↔ (sexo 'F' ∧ 60 <= edad) }
  asegura: { (res = "Anda de vacaciones") ↔ (sexo 'M' ∧ 63 <= edad) }
  asegura: { (res = "Te toca trabajar") ↔ (sexo = 'F' ∧ 18 <= edad < 60) }
  asegura: { (res = "Te toca trabajar") ↔ (sexo = 'M' ∧ 18 <= edad < 63) }
}
"""
def clasifica_edad_sexo(sexo: str, edad: int) -> str: # Version con operaciones logicas
  if edad < 18:
    print('Anda de vacaciones')
  elif edad >= 63 and sexo == 'M':
    print('Anda de vacaciones')
  elif edad >= 60 and sexo == 'F':
    print('Anda de vacaciones')
  elif edad > 17:
    print('Te toca trabajar')


def clasifica_edad_sexoV2(sexo: str, edad: int) -> str: # Version con if anidados
  if edad < 18:
    print('Anda de vacaciones')
  if sexo == 'M':
    if edad >= 63:
      print('Anda de vacaciones')
    else:
      print('Te toca trabajar')
  elif sexo == 'F':
    if edad >= 60:
      print('Anda de vacaciones')
    else:
      print('Te toca trabajar')


# Ejericio 6
""""
Implementar los siguientes procedimientos usando repeticion condicional while:
"""
# 6.1
"""
Escribir un procedimiento que imprima los numeros del 1 al 10
"""
def conteo1a10():
  i = 1
  while i < 11:
    print(i)
    i += 1

# 6.2
"""
Escribir un procedimiento que imprima los numeros pares entre el 10 y el 40
"""
def pares_entre10y40():
  i = 10
  while i < 41:
    if es_multiplo_de(i,2):
      print(i)
      i += 1
    else:
      i += 1

# 6.3
"""
Escribir un procedimiento que imprima la palabra "eco" 10 veces
"""
def eco10():
  i = 0
  while i < 10:
    print('eco')
    i += 1

# 6.4
"""
Escribir un procedimiento de cuenta regresiva para lanzar un cohete. Dicho procedimiento ira imprimiendo desde el numero
que me pasan por parametro (que sera positivo) hasta el 1, y por ultimo 'Despegue'
"""
def cuenta_regresiva(desde: int):
  while desde > 0:
    print(desde)
    desde -= 1
  print('Despegue')

# 6.5
"""
Hacer un procedimiento que monitoree un viaje en el tiempo. Dicho procedimiento recibe dos parametros, "el año de partida"
y "algun año de llegada", siendo este ultimo parametro siempre mas chico que el primero. El viaje se realizara de a saltos de un año
y el procedimiento debe mostrar el texto: "Viajo un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de año.
"""
def viaje_en_el_tiempo(partida: int, llegada: int):
  partida -= 1
  while llegada <= partida:
    print(f'Viajo un año al pasado, estamos en el año: {partida}')
    partida -= 1

# 6.6
"""
Implementar de nuevo el procedimiento de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo mas cercano
al 384 a.C., donde conoceremos a Aristoteles. Y para que sea mas rapido el viaje, ¡Vamos a viajar de a 20 años en cada salto!
"""
def viaje_aristoteles(partida: int):
  partida_dc = partida - 20
  while partida_dc >= 1:
    print(f'Viajo veinte años al pasado, estamos en el año: {partida_dc} d.C.')
    partida_dc -= 20
  partida_dc += 20
  partida_ac = -(partida_dc - 21)
  while partida_ac <= 384:
    print(f'Viajo veinte años al pasado, estamos en el año: {partida_ac} a.C.')
    partida_ac += 20

# Ejercicio 7
"""
Implementar los procedimientos del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la funcion range
para generar una secuencia de numeros en un rango dado, con un valor inicial i, un valor final f y un paso p. Ver documentacion.
"""
# 7.1 - conteo1a10():
def conteo1a10v2():
  for num in range (1,11,1):
    print(num)

# 7.2 - pares_entre10y40():
def pares_entre10y40v2():
  for num in range (10,41,2):
    print(num)

# 7.3 - eco10():
def eco10v2():
  for num in range(0,10,1):
    print('eco')

# 7.4 - cuenta_regresiva():
def cuenta_regresivaV2(inicio: int) -> int:
  for num in range(0,inicio,1):
    print(-(num - inicio))
  print('Despegue')

# 7.5 - viaje_en_el_tiempo():
def viaje_en_el_tiempoV2(partida: int, llegada: int) -> str:
  rango = range(llegada , partida,1)
  primerSalto = partida - 1
  for num in rango:
    print(f'Viajo un año al pasado, estamos en el año: {primerSalto - rango.index(num)}')

# 7.6 - viaje_aristoteles():
def viaje_aristotelesV2(partida: int) -> str:
  cantidadSaltos_dc = partida // 20
  for num in range(0, cantidadSaltos_dc,1):
    partida -= 20
    print(f'Viajo veinte años al pasado, estamos en el año: {partida} d.C.')
  partida_ac = -(partida - 21)
  for num in range(partida_ac, 385,20):
    print(f'Viajo veinte años al pasado, estamos en el año: {num} a.C.')

# Ejercicio 8 - Realizar la ejecucion simbolica de los siguientes codigos:

# 8.1 - x=5 ; y=7 ; x = x + y
x=5          # Estado a: x vale 5

y=7          # Estado b: x vale 5, y vale 7

x = x + y    # Estado c: y vale 7, x vale 5+7=12

# 8.2 - x=5 ; y=7 ; z=x+y ; y = z * 2
x=5          # Estado a: x vale 5

y=7          # Estado b: x vale 5, y vale 7

z = x + y    # Estado c: x vale 5, y vale 7, z vale 5+7=12

y = z * 2    # Estado d: x vale 5, y vale 12*2=24, z vale 12

# 8.3 - x=5 ; y=7 ; x="hora" ; y = x * 2
x=5          # Estado a: x vale 5

y=7          # Estado b: x vale 5, y vale 7

x="hora"     # Estado c: x vale "hora", y vale 7

y = x * 2    # Estado d: x vale "hora", y vale "horahora"

# 8.4 - x=False ; res=not(x)
x=False      # Estado a: x vale False

res=not(x)   # Estado b: x vale False, res vale not(False)=True

# 8.5 - x=False ; x=not(x)
x=False      # Estado a: x vale False

x=not(x)     # Estado b: x vale not(False)=True

# 8.6 - x=True ; y=False ; res=x and y ; x = res and x
x=True        # Estado a: x vale True

y=False       # Estado b: x vale True, y vale False

res=x and y   # Estado c: x vale True, y vale False, res vale (True and False) = False

x = res and x # Estado d: x vale (False and True) = False, y vale False, res vale False

# Ejercicio 9 - Sea el siguiente codigo:
"""
def rt(x:int, g:int) -> int:
  g = g + 1
  return x + g

g: int = 0
def ro(x: int) -> int:
  global g
  g = g + 1
  return x + g
"""

# 9.1 - ¿Cual es el resultado de evaluar tres veces seguidas ro(1)?
"""
Primera vez: global g = 0 -> g = 0 + 1 = 1-> returns 1 + 1 = 2

Segunda vez: global g = 1 -> g = 1 + 1 = 2 -> returns 1 + 2 = 3

Tercera vez: global g = 2 -> g = 2 + 1 = 3 -> returns 1 + 3 = 4
"""

# 9.2 - ¿Cual es el resultado de evaluar tres veces seguidas rt(1, 0)?
"""
Primera vez: g = 0 + 1 = 1 -> returns 1 + 1 = 2

Segunda vez: g = 0 + 1 = 1 -> returns 1 + 1 = 2

Tercera vez: g = 0 + 1 = 1 -> returns 1 + 1 = 2
"""

# 9.3 - En cada funcion, realizar la ejecucion simbolica.
def rt(x:int, g:int) -> int:
  # Estado a: x vale x, g vale g
  g = g + 1
  # Estado b: x vale x, g vale g@a+1
  return x + g

g: int = 0
# Estado x = g vale 0
def ro(x: int) -> int:
  global g
  # Estado a: g vale global g
  g = g + 1
  # Estado b: g vale g@a+1
  return x + g

# 9.4 - Dar la especificacion para cada funcion, rt y ro.
"""
problema rt ( in x: Integer, in g: Integer ) : Integer {
  requiere: {x, g ∈ Z}
  asegura: { (g + 1) + x }
}

problema ro ( in x: Integer ) : Integer {
  requiere: {x ∈ Z}
  requiere: {g es una variable definida en el programa}
  asegura: { (g + 1) + x }
}
"""
