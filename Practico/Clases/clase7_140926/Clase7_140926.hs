module Clase7 where

-- Ejercicios de clase anterior 09/09

-- Ejercicio 8

-- multiplicarFilas :: [[Integer]] -> [Integer] segun la
-- siguiente especificacion:
-- problema multiplicarFilas (m: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
--     requiere: { |m| > 0 }
--     requiere: { |m[0]| > 0 }
--     requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
--     asegura: {|res| = |m|}asegura: {Para todo 0 ≤ i < |res|, res[i]= Q|m[0]|−1 j=0 m[i][j]}
-- }
-- Por ejemplo, multiplicarFilas [[1,2],[3,4]] es igual a [2,12]

multiplicarFilas :: [[Integer]] -> [Integer]
multiplicarFilas (f:[]) = [multiFila f]
multiplicarFilas (f:fs) = [multiFila f] ++ multiplicarFilas fs

multiFila :: [Integer] -> Integer
multiFila (x:[]) = x
multiFila (x:xs) = x * multiFila xs

-- Ejercicio 8.2

-- Implementar la función cantidadDeApariciones :: Integer ->[[Integer]] -> Integer según la siguiente especificación:
-- problema cantidadDeApariciones (e: Z, m: seq⟨seq⟨Z⟩⟩) : Z {
--     requiere: { |m| > 0 }
--     requiere: { |m[0]| > 0 }
--     requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
--     asegura: {P|m|−1 P|m[i]|−1 1 si m[i][j] es igual a e, 0 si no resultado = i=0 j=0}
-- }
-- Por ejemplo, cantidadDeApariciones 1 [[1,0],[0,1]] es igual a 2.

cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones e (f:[]) = cantidadDeAparicionesFila e f
cantidadDeApariciones e (f:fs) = cantidadDeAparicionesFila e f + cantidadDeApariciones e fs


cantidadDeAparicionesFila :: Integer -> [Integer] -> Integer
cantidadDeAparicionesFila e (x:[])  | e == x = 1
                                    | otherwise = 0
cantidadDeAparicionesFila e (x:xs)  | e == x = 1 + cantidadDeAparicionesFila e xs
                                    | otherwise = cantidadDeAparicionesFila e xs


-- Ejercicios clase actual 14/09

-- Ver clase7test.hs
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 1)
