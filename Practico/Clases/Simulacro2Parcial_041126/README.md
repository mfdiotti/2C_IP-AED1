# Simulacro 2do Parcial - Python

Simulacro previo al segundo parcial, realizado en 2:30h (1h menos que el parcial definitivo).

## Archivos

```Tree
Simulacro2Parcial_041126/
├── correcciones/              # Correcciones propias realizadas post devolucion
│   └── submission.py
├── enunciado.md               # Enunciado de ejercicios
├── README.md
└── submission.py              # Solucion enviada
```

## Construcciones Validas - Python

Listado de funciones que pueden utilizar para el parcial de Python. Cualquier otra funcion debe ser implementada. Si utilizan una funcion no permitida, se anula el ejercicio.

```Python
  conversion de tipos: (int, list, float, str, tuple, bool)
  estructuras: (if-else-elif, while, for) // Pueden usar for in range(..) o for in secuencia
  Rango: range(i,f,p) // Pueden usar los 3 parametros, 2 o 1.
  arimeticas (+, -, *, /, //, sqrt, round, floor, ceil, %)
  logicas (and, or, not, ==, !=, >, <, >=, <=)
  Sobre secuencias
  pertenece: in
  concatenacion: +
  repeticion: *
  longitud: len
  acceso a elementos: s[elem] // No esta permitido s[i:f], s[-i] o similar!
  Listas: append(e), insert(p, e), remove(e), index(e), count(e), clear(), pop(), pop(n), copy()
  Diccionarios: items(), keys(), values(), pop(clave), clear()
  TAD Pilas: from queue import LifoQueue
  pila = LifoQueue(); put(e); get(); empty()
  TAD Colas: from queue import Queue
  cola = Queue(); put(e); get(); empty()
  Archivos: open, read, readline, readlines, write, writelines, close, os.path.join(), os.path.exists()
```

### Aclaraciones

- El uso de break/continue NO esta recomendado.
- Recordar que todas las variables deben ir anotadas con su tipo correspondiente.
