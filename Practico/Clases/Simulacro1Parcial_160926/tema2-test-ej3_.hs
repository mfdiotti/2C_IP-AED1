import SolucionT2
import Test.HUnit
import Data.List

main3 = runTestTT allTests

allTests = test[
    "Lista vacía" ~: f3 [] 5 ~?= [],
    "Ningún elemento supera el umbral" ~: f3 [1, 2, 3, 4] 5 ~?= [1, 2, 3, 4],
    "Algunos elementos superan el umbral" ~: f3 [3, 6, 2, 9] 5 ~?= [3, 5, 2, 5],
    "Todos los elementos superan el umbral" ~: f3 [6, 7, 8] 5 ~?= [5, 5, 5],
    "Lista con todos iguales al umbral" ~: f3 [5, 5, 5] 5 ~?= [5, 5, 5],
    "Lista con un solo elemento menor al umbral" ~: f3 [3] 5 ~?= [3],
    "Lista con un solo elemento igual al umbral" ~: f3 [5] 5 ~?= [5],
    "Lista con un solo elemento mayor al umbral" ~: f3 [7] 5 ~?= [5],
    "Lista con valores mixtos y umbral positivo" ~: f3 [199, 0, 1, 2, 3, 4, 5, 6] 3 ~?= [3,0,1,2,3,3,3,3],
    "Lista con valores grandes" ~: f3 [1000, 2000, 3000] 1500 ~?= [1000, 1500, 1500],
    "Lista con un negativo al final" ~: f3 [3, 6, 2, 9, -1] 5 ~?= [3, 5, 2, 5],
    "Lista con varios negativos al final" ~: f3 [3, 6, 2, 9, -1, -4, -6] 5 ~?= [3, 5, 2, 5],
    "Lista con varios negativos al principio" ~: f3 [-1, -4, -6, 3, 6, 2, 9] 5 ~?= [],
    "Lista con positivos después de negativos" ~: f3 [3, 6, 2, 9, -1, -4, 6] 5 ~?= [3, 5, 2, 5],
    "Lista con todos negativos" ~: f3 [-1, -4, -6] 5 ~?= []
    ]
