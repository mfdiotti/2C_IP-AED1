from queue import LifoQueue as Pila
from typing import TypeVar
T = TypeVar('T')
import random

# Ej 16
def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
    notas_copia: list[tuple[str,float]] = notas.copy()
    res: dict[str,float] = {}
    
    while notas_copia != []:
        nombre: str = notas_copia[0][0]
        suma_notas: float = 0
        cantidad_notas: int = 0
        
        for nota in notas_copia:
            if nota[0] == nombre:
                suma_notas += nota[1]
                cantidad_notas += 1
        
        promedio: float = suma_notas / cantidad_notas
        res[nombre] = promedio

        for nota in notas:
            if nota[0] == nombre:
                notas_copia.remove(nota)

    return res


# Ej 17
# 17.1
historiales: dict[str,Pila[str]] = {}

#17.2
def visitar_sitio(historiales: dict[str,Pila[str]], usuario: str, sitio: str) -> None:
    usuarios: list[str] = list(historiales.keys())

    if usuario in usuarios:
        historiales[usuario].put(sitio)
    else:
        sitios_visitados: Pila[str] = Pila()
        sitios_visitados.put(sitio)
        historiales[usuario] = sitios_visitados


# 17.3
def navegar_atras(historiales: dict[str,Pila[str]],usuario: str) -> str:
    return historiales[usuario].get()

### Auxiliar para leer pilas
def pila_a_lista(p: Pila[T]) -> list[T]:
  pila_temp: Pila[T] = Pila()
  res: list[T] = []
  
  while not p.empty():
    ultimo_elemento: T = p.get()
    pila_temp.put(ultimo_elemento)
    res.append(ultimo_elemento)

  while not pila_temp.empty():
    p.put(pila_temp.get())

  return res
