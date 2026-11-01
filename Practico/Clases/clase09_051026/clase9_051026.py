def hola():
    print("hola")

def cuenta_regresiva_solo_pares_y_es_par(num: int) -> bool:
    #Cuenta regresiva desde num hasta 0
    #Devuelve si num es par
    if num % 2 != 0:
        num -= 1
        valor: bool = False
    else:
        valor:bool = True
    
    for i in range(num,0,-2):
        print(i)
    
    return valor
