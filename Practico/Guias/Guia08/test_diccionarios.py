import unittest
from diccionarios import *


class TestPromedio(unittest.TestCase):
    def test_unico(self):
        notas = [("juan", 8.0)]
        resultado_esperado = {"juan": 8.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)

    def test_varios_no_repetidos(self):
        notas = [("juan", 8.0),("jose",9.0),("sofia",10.0)]
        resultado_esperado = {"juan": 8.0,"jose": 9.0,"sofia": 10.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)

    def test_varios_repetidos(self):
        notas = [("juan", 8.0),("jose",9.0),("sofia",10.0),("jose", 7.0),("juan",9.0),("sofia",10.0),("luna",7.0)]
        resultado_esperado = {"juan": 8.5,"jose": 8.0,"sofia": 10.0, "luna": 7.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)


class test_visitar_sitio(unittest.TestCase):
    def test_comienza_sin_usuarios_en_historiales(self):
        historiales: dict[str,Pila[str]] = {}
        usuario: str = 'user'
        sitio: str = 'google.com'
        
        visitar_sitio(historiales,usuario,sitio)

        pila_sitios: list[str] = pila_a_lista(historiales[usuario])
        lista_usuarios: list[str] = list(historiales.keys())

        self.assertEqual([sitio],pila_sitios)
        self.assertEqual([usuario],lista_usuarios)
        self.assertNotEqual(historiales,{})

    def test_ya_hay_un_usuario_y_se_agrega_sitio(self):
        historiales: dict[str,Pila[str]] = {'user':Pila()}
        sitio1: str = 'github.com'
        historiales['user'].put(sitio1)
        
        usuario: str = 'user'
        sitio2: str = 'google.com'
        
        visitar_sitio(historiales,usuario,sitio2)

        pila_sitios: list[str] = pila_a_lista(historiales[usuario])
        lista_usuarios: list[str] = list(historiales.keys())

        self.assertEqual([sitio2,sitio1],pila_sitios)
        self.assertEqual([usuario],lista_usuarios)
        self.assertNotEqual(historiales,{})

    def test_sin_usuarios_se_agregan_varios(self):
        historiales: dict[str,Pila[str]] = {}
        
        usuario1: str = 'user1'
        usuario2: str = 'user2'
        usuario3: str = 'user3'
        sitio1: str = 'google.com'
        sitio2: str = 'github.com'
        
        visitar_sitio(historiales,usuario1,sitio1)
        visitar_sitio(historiales,usuario1,sitio2)
        visitar_sitio(historiales,usuario2,sitio2)
        visitar_sitio(historiales,usuario3,sitio2)
        visitar_sitio(historiales,usuario3,sitio1)
        
        pila_sitios_usuario1: list[str] = pila_a_lista(historiales[usuario1])
        pila_sitios_usuario2: list[str] = pila_a_lista(historiales[usuario2])
        pila_sitios_usuario3: list[str] = pila_a_lista(historiales[usuario3])
        lista_usuarios: list[str] = list(historiales.keys())

        self.assertEqual([sitio2,sitio1],pila_sitios_usuario1)
        self.assertEqual([sitio2],pila_sitios_usuario2)
        self.assertEqual([sitio1,sitio2],pila_sitios_usuario3)
        self.assertEqual([usuario1,usuario2,usuario3],lista_usuarios)
        self.assertNotEqual(historiales,{})


class test_navegar_atras(unittest.TestCase):
    def test_un_usuario_con_dos_sitios(self):
        historiales: dict[str,Pila[str]] = {'user':Pila()}
        usuario: str = 'user'
        sitio1: str = 'github.com'
        sitio2: str = 'google.com'
        historiales[usuario].put(sitio1)
        historiales[usuario].put(sitio2)

        # Verifica estado anterior del diccionario: Diccionario bien formado
        pila_sitios_pre: list[str] = pila_a_lista(historiales[usuario])
        lista_usuarios_pre: list[str] = list(historiales.keys())

        self.assertEqual([sitio2,sitio1],pila_sitios_pre)
        self.assertEqual([usuario],lista_usuarios_pre)

        # Verifica estado posterior del diccionario y resultado: navegar_sitio funciona como se espera
        res: str = navegar_atras(historiales,usuario)
        pila_sitios_post: list[str] = pila_a_lista(historiales[usuario])
        lista_usuarios_post: list[str] = list(historiales.keys())

        self.assertEqual([sitio1],pila_sitios_post)
        self.assertEqual([usuario],lista_usuarios_post)
        self.assertEqual(res,sitio2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
