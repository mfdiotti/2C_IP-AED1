--Ejercicio 4 b)
esParMenor :: (Float,Float)->(Float,Float)->Bool
esParMenor a b | fst a < fst b && snd a < snd b = True
    | otherwise = False

esParMenor2 :: (Float,Float)->(Float,Float)->Bool
esParMenor2 (a,b) (c,d) | a<c && b<d = True
    | otherwise = False

type Punto2D = (Float,Float)
esParMenor3 :: Punto2D->Punto2D->Bool
esParMenor3 a b | fst a < fst b && snd a < snd b = True
    | otherwise = False


--Ejercicio 4 f)
posPrimerPar :: (Integer,Integer,Integer)->Integer
posPrimerPar (a,b,c) | mod a 2 == 0 = 1
    | mod b 2 == 0 = 2
    | mod c 2 == 0 = 3
    | otherwise = 4

--Ejercicio 6
esMultiplo :: Integer->Integer->Bool
esMultiplo x y | mod x y == 0 = True
    | otherwise = False

bisiesto :: Integer->Bool
bisiesto yr | esMultiplo yr 400 = True
    | esMultiplo yr 100 = False
    | esMultiplo yr 4 = True
    | otherwise = False

--Ejercicio 7
type Coordenada3d = (Float,Float,Float)
absoluto :: Float->Float
absoluto x | x < 0 = -x
    | otherwise = x

distanciaManhattan :: Coordenada3d->Coordenada3d->Float
distanciaManhattan (a,b,c) (x,y,z) = (absoluto (a-x)) + (absoluto (b-y)) + (absoluto (c-z))

--Ejercicio 8
digitoUnidades :: Integer->Integer
digitoUnidades x = mod x 10

digitoDecenas :: Integer->Integer
digitoDecenas x = div (mod x 100) 10

sumaUltimosDosDigitos :: Integer->Integer
sumaUltimosDosDigitos x = (digitoDecenas x) + (digitoUnidades x)

comparar :: Integer->Integer->Integer
comparar x y | (sumaUltimosDosDigitos x) < (sumaUltimosDosDigitos y) = 1
    | (sumaUltimosDosDigitos x) > (sumaUltimosDosDigitos y) = -1
    | (sumaUltimosDosDigitos x) == (sumaUltimosDosDigitos y) = 0
