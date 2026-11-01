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
