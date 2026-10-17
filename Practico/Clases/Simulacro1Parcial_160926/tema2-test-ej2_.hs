import SolucionT2
import Test.HUnit
import Data.List

main2 = runTestTT allTests

allTests = test[
    "Lista vacía" ~: f2 [] ~?= [],
    "Ninguna cursada vencida" ~: f2 [("Álgebra", 2022, 1), ("Análisis", 2023, 2)] ~?= [],
    "Una vencida y otra no" ~: f2 [("Álgebra", 2020, 2), ("Análisis", 2021, 2)] ~?= ["Álgebra"],
    "Todas las cursadas vencidas" ~: expectPermutacion (f2 [("Álgebra", 2020, 2), ("Análisis", 2019, 1)])["Álgebra", "Análisis"],
    "Solo una cursada y no vencida" ~: f2 [("Álgebra", 2022, 2)] ~?= [],
    "Solo una cursada y vencida" ~: f2 [("Introducción a la Programación", 2020, 1)] ~?= ["Introducción a la Programación"],
    "Cursada en el limite no vencida" ~: f2 [("Introducción a la Programación", 2021, 2)] ~?= [],
    "Cursada en el limite vencida" ~: f2 [("Introducción a la Programación", 2021, 1)] ~?= ["Introducción a la Programación"],
    "Cursada de 1993" ~: f2 [("Taller de Álgebra", 1993, 0)] ~?= ["Taller de Álgebra"],
    "Materias vencidas repetidas, devuelve sin repetidos" ~: f2 [("M1", 2010, 1), ("M1", 2020, 1)] ~?= ["M1"]
    ]

-- ------------ FUNCIONES AUXILIARES ------------
-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)
expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)
