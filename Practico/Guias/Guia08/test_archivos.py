import unittest
from archivos import *

class TestContarLineas(unittest.TestCase):
    def test_contar_lineas_archivo_vacio(self):
        archivo = "archivos_test/archivo_vacio.txt"
        resultado = contar_lineas(archivo)
        self.assertEqual(resultado, 0)
    
    def test_contar_lineas_una_linea(self):
        archivo = "archivos_test/archivo_con_una_linea.txt"
        resultado = contar_lineas(archivo)
        self.assertEqual(resultado, 1)
    
    def test_contar_lineas_con_cinco_lineas(self):
        archivo = "archivos_test/archivo_con_lineas.txt"
        resultado = contar_lineas(archivo)
        self.assertEqual(resultado, 5)
    
    def test_contar_lineas_una_linea_vacia(self):
        archivo = "archivos_test/archivo_una_linea_vacia.txt"
        resultado = contar_lineas(archivo)
        self.assertEqual(resultado, 1)


class TestClonarSinComentarios(unittest.TestCase):
    def test_clonar_archivo_vacio(self):
        archivo_entrada = "archivos_test/archivo_vacio.txt"
        archivo_salida = "archivos_test/archivo_salida.txt"
        clonar_sin_comentarios(archivo_entrada, archivo_salida)
        f = open(archivo_salida, 'r')
        contenido = f.read()
        f.close()
        self.assertEqual(contenido, "")

    def test_clonar_archivo_con_comentarios(self):
        archivo_entrada = "archivos_test/archivo_con_comentarios.txt"
        archivo_salida = "archivos_test/archivo_salida.txt"
        clonar_sin_comentarios(archivo_entrada, archivo_salida)
        f = open(archivo_salida, 'r')
        contenido = f.read()
        f.close()
        self.assertEqual(contenido, "Esto no es un comentario\nEsto tampoco # este tampoco\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
