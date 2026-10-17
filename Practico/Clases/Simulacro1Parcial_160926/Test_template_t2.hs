import Test.HUnit
import SolucionT2

main = runTestTT tests

tests = test [
    -- "nombre" ~: (funcion parametros) ~?= resultado_esperado
    "Rango que incluye varios abundantes" ~: f1 12 24 ~?= 4,
    "de 1 a 100" ~: f1 1 100 ~?= 22
    ]