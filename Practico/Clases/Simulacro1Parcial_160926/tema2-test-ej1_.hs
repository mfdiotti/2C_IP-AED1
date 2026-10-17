import SolucionT2
import Test.HUnit
import Data.List

main1 = runTestTT allTests

allTests = test[
    -- Casos base y casos sin numeros abundantes
    "Rango sin números abundantes" ~: f1 3 4 ~?= 0,
    "Rango de un solo número no abundante" ~: f1 5 5 ~?= 0,
    "Rango pequeño sin abundantes" ~: f1 1 5 ~?= 0,
    "Los primeros 11 números son no abundantes" ~: f1 1 11 ~?= 0,
    -- Casos con numeros abundantes
    "Rango con un número abundante" ~: f1 29 30 ~?= 1,
    "Rango con un número abundante, d y h iguales" ~: f1 30 30 ~?= 1,
    "Rango con varios números abundantes" ~: f1 3 30 ~?= 5,
    "Rango de un solo número abundante (grande)" ~: f1 198126 198126 ~?= 1,
    "Rango que incluye varios abundantes (enunciado)" ~: f1 12 24 ~?= 4,
    "Rango donde d y h son ambos abundantes" ~: f1 18 30 ~?= 4,
    "Rango donde solo el límite superior es abundante" ~: f1 10 12 ~?= 1,
    "Rango donde solo el límite inferior es abundante" ~: f1 12 14 ~?= 1,
    "Rango grande" ~: f1 30 198 ~?= 41
    ]
