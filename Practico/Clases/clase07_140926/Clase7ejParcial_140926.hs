mayorNumeroConNDivisores :: Integer -> Integer -> Integer -> Integer
mayorNumeroConNDivisores d h n  | tieneNDivisores n h = h
                                | otherwise = mayorNumeroConNDivisores d (h-1) n

tieneNDivisores :: Integer -> Integer -> Bool
-- en lumero m tiene n divisores
tieneNDivisores n m = cantDivisores m == n

cantDivisores :: Integer -> Integer
cantDivisores m = cantDivisoresDesde m 1

cantDivisoresDesde :: Integer -> Integer -> Integer
-- requiere d <= m
cantDivisoresDesde m d  | m == d = 1
                        | mod m d == 0 = 1 + cantDivisoresDesde m (d+1)
                        | otherwise = cantDivisoresDesde m (d+1)