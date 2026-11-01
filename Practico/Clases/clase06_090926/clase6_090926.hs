-- LONGITUD

-- longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos

-- problema longitud (s: seq⟨T⟩) : Z {
--     requiere: { True }
--     asegura: { resultado = cantidad de elementos de s }
-- }

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs


-- SUMATORIA

-- problema sumatoria (s: seq⟨Z⟩) : Z {
--     requiere: { True }
--     asegura: { resultado = suma cada elemento de la lista }
-- }

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- EN GRUPOS

-- problema f2 (n:Z, s: seq⟨Z⟩) : {
--     requiere: { True }
--     asegura: { |resultado| = |s| ∧ cada posicion de resultado contiene el valor 
--                                          que hay en esa posicion en s sumado n }
-- }

f2 :: Integer -> [Integer] -> [Integer]
f2 n [] = []
f2 n (x:xs) = [(x+n)] ++ f2 n xs

-- AUX F1-pertenece (otro prob)

f1 :: (Eq t) => t -> [t] -> Bool
f1 _ [] = False
f1 y (x:xs) | y == x = True
            | otherwise = f1 y xs


-- Ejercicio 2.5

-- Implementar quitar :: (Eq t) => t -> [t] -> [t], que dados un elemento e 
-- y una lista s, elimina la primera aparicion de e en la lista s (de haberla).

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar y (x:xs) | y /= x = x : quitar y xs
                | otherwise = xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos y (x:xs)    | y /= x = x : quitarTodos y xs
                        | otherwise = quitarTodos y xs


-- Ejercio 3.3 

-- problema maximo (s: seq⟨Z⟩) : Z {
--     requiere: { |s| > 0 }
--     asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
-- }

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:(y:xs))   | x > y = maximo (x:xs)
                    | otherwise = maximo (y:xs)


-- Ejercicio 3.9

-- problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
--     requiere: { True }
--     asegura: { resultado contiene los elementos de s ordenados deforma creciente }
-- }

-- ordenar :: [Integer] -> [Integer]
-- ordenar [] = []
-- ordenar [x] = [x]
-- ordenar (x:(y:xs))  | x < y = reverse (ordenar(y:(ordenar(x:xs))))
--                     | otherwise = reverse (ordenar(x:(ordenar(x:xs))))

ordenarMayorAMenor :: [Integer] -> [Integer]
ordenarMayorAMenor [] = []
ordenarMayorAMenor xs = maximo xs : ordenarMayorAMenor (quitar (maximo xs) xs)

ordenarMenorAMayor :: [Integer] -> [Integer]
ordenarMenorAMayor xs = reverso (ordenarMayorAMenor xs)

reverso :: [Integer] -> [Integer]
reverso [] = []
reverso (x:xs) = reverso (xs) ++ [x]
