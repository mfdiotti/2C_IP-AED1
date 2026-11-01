-- Ejercicios guia 4 clase del mie 02/09 (Recursion sobre enteros p1)

eliminarUnidades :: Int -> Int
eliminarUnidades x = div x 10

digitoUnidades :: Int -> Int
digitoUnidades x = div x 10

iesimoDigito :: Int -> Int -> Int
iesimoDigito x i    | i == cantidadDeDigitos x = digitoUnidades x
                    | otherwise = iesimoDigito (eliminarUnidades x ) i

cantidadDeDigitos :: Int -> Int
cantidadDeDigitos x | x < 10 = 1
                    | otherwise = 1 + cantidadDeDigitos (eliminarUnidades x)

--VER!!!!!!!!!!
esCapicua :: Int -> Bool
esCapicua n = esCapicuaDesde n 1

esCapicuaDesde :: Int -> Int -> Bool
esCapicuaDesde n i  | i > cantidadDeDigitos n - i + 1 = True
                    | otherwise = iesimoDigito n i == iesimoDigito n (cantidadDeDigitos n - i + 1) && esCapicuaDesde n (i + 1)

-- Ejercicios guia 4 clase lun 07/09 (Recursion sobre enteros p2)
-- Del teorico de jue 27/08
sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j - 1)

-- Del teorico de jue 27/08
sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaDoble (n - 1) m + sumatoriaInterna n m


--Ejercicio 14 
--Especificar e implementar una funcion sumaPotencias :: Integer -> Integer -> Integer -> Integer que
-- dados tres naturales q, n, m sume todas las potencias de la forma q^(a+b) con 1 ≤ a ≤ n y 1 ≤ b ≤ m
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 b = sumaPotenciasInterna q 1 b
sumaPotencias q a b = sumaPotencias q (a - 1) b + sumaPotenciasInterna q a b

sumaPotenciasInterna :: Integer -> Integer -> Integer -> Integer
sumaPotenciasInterna q a 1 = q ^ (a + 1)
sumaPotenciasInterna q a b = q ^ (a + b) + sumaPotenciasInterna q a (b - 1)

--Ejercicio 16
--Implementar menorDivisor :: Integer -> Integer que calcule el menor divisor (mayor que 1) de un natural n pasado como parametro.

menorDivisor :: Integer -> Integer
menorDivisor n  | n == 1 = 1
                | otherwise = buscaMenorDivisorDesde 2 n

buscaMenorDivisorDesde :: Integer -> Integer -> Integer
buscaMenorDivisorDesde i n  | i == n = i
                            | mod n i == 0 = i
                            | otherwise = buscaMenorDivisorDesde (i + 1) n

--Ejercicio 19
-- esSumaInicialDePrimos :: Integer -> Bool
-- esSumaInicialDePrimos n = True
-- 
-- iesimaSumaPrimo 1 = 2
-- iesimaSumaPrimo i = 
