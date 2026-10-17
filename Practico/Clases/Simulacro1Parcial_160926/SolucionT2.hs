module SolucionT2 where

-- Ejercicio 1
f1 :: Integer -> Integer -> Integer
f1 d h  | h == d && esAbundante d h = 1
        | h == d && not (esAbundante d h) = 0
        | esAbundante d h = 1 + f1 d (h-1)
        | otherwise = 0 + f1 d (h-1)

esDivisor :: Integer -> Integer -> Bool
-- es divisor n de m
esDivisor n m   | mod m n == 0 = True
                | otherwise = False

sumaDivisores :: Integer -> Integer -> Integer
sumaDivisores d h   | d == h = 0
                    | esDivisor d h = d + sumaDivisores (d+1) h
                    | otherwise = sumaDivisores (d+1) h

esAbundante :: Integer -> Integer -> Bool
esAbundante d h | sumaDivisores 1 h > h = True
                | otherwise = False

-- Ejercicio 2
-- f2 :: [(String, Integer, Integer)] -> [String]


-- Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]
f3 xs u = reemplazaMayoresPorU (listaHastaNegativo xs) u

reemplazaMayoresPorU :: [Integer] -> Integer -> [Integer]
reemplazaMayoresPorU [] u = []
reemplazaMayoresPorU (x:xs) u | x > u = u : (reemplazaMayoresPorU xs u)
            | otherwise = x : (reemplazaMayoresPorU xs u)

listaHastaNegativo :: [Integer] -> [Integer]
listaHastaNegativo [] = []
listaHastaNegativo (x:xs)   | x >= 0 = x : [] ++ listaHastaNegativo xs
                            | otherwise = []

-- Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 _ _ = 0
