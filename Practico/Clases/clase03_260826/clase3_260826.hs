
doubleMe :: Integer -> Integer
doubleMe x = x + x

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

h :: Integer -> Integer
h x = f (g x)

k :: Integer -> Integer
k x = g (f x)

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x > y && x > z = x
    | y > x && y > z = y
    | otherwise = z


sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z
    | (x == y) && (x /= z) && (y /= z) = z
    | (x /= y) && (x == z) && (y /= z) = y
    | (x /= y) && (x /= z) && (y == z) = x
    | (x == y) && (x == z) && (y == z) = 0

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

digitoDecenas :: Integer -> Integer
digitoDecenas x = mod (div x 10) 10