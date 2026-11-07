# Simulacro 1er Parcial - Haskell

Simulacro previo al primer parcial, realizado en 2:30h (1h menos que el parcial definitivo).

## Archivos

```Tree
Simulacro1Parcial_160926/
├── enunciado.md               # Enunciado de ejercicios
├── README.md
├── SolucionT2.hs              # Solucion enviada
├── Test_template_t2.hs        # Tests utilizados durante el simulacro
└── tema2-test-ejX_.hs         # Test brindados post correcion por la catedra
```
## Funciones Validas

Listado de funciones que pueden utilizar para el parcial de Haskell. Cualquier otra función debe ser implementada. Si utilizan una función no permitida, se anula el ejercicio.

```haskell
  mod :: Integral a => a -> a -> a
  div :: Integral a => a -> a -> a
  fst :: (a, b) -> a
  snd :: (a, b) -> b
  sqrt :: Floating a => a -> a
  (:) :: a -> [a] -> [a]
  (++) :: [a] -> [a] -> [a]
  head :: [a] -> a
  tail :: [a] -> [a]
  fromIntegral :: (Integral a, Num b) => a -> b
  fromInteger :: Num a => Integer -> a
  not :: Bool -> Bool
  -- ariméticas (+,-,*,/)
  -- potencia (**,^)
  -- lógicas (&&,||,==,/=,>,<,>=,<=)
```

### Aclaraciones

- No está permitido el uso del condicional “if then else”.
- El uso de where está permitido
