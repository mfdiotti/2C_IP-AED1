from queue import Queue as Cola

def ejercicio1(s: list[int]) -> list[int]:
    subsecuencias: list[tuple[int,int]] = []
    i: int = 0

    subsecuencia: list[int] = []
    indice_inicio: int = 0
    
    while i < len(s)-1:
        if len(subsecuencia) == 0:
            indice_inicio = i
            subsecuencia.append(s[i])

        if s[i] < s[i+1]:
            subsecuencia.append(s[i])
        else:
            subsecuencias.append((indice_inicio,len(subsecuencia)))
            subsecuencia = []

        i += 1

    if len(subsecuencia) > 0:
        subsecuencias.append((indice_inicio,len(subsecuencia)))

    indice: int = 0
    maxima_longitud: int = 0

    for datos_subseq in subsecuencias:
        if datos_subseq[1] > maxima_longitud:
            maxima_longitud = datos_subseq[1]
            indice = datos_subseq[0]

    indice_ultimo_num_en_subseq: int = indice + maxima_longitud
    res: list[int] = []

    for i in range(indice,indice_ultimo_num_en_subseq):
        res.append(s[i])

    return res


def ejercicio2(pedidos: Cola[tuple[str,int]], stock: int) -> Cola[str]:
    despachados_lista: list[str] = []
    no_despachados_lista: list[tuple[str,int]] = []
    stock_restante: int = stock

    while not pedidos.empty():
        pedido: tuple[str,int] = pedidos.get()

        if pedido[1] <= stock_restante:
            despachados_lista.append(pedido[0])
            stock_restante -= pedido[1]
        else:
            no_despachados_lista.append(pedido)

    res: Cola[str] = Cola()

    for despachado in despachados_lista:
        res.put(despachado)

    for no_despachado in no_despachados_lista:
        pedidos.put(no_despachado)

    return res
