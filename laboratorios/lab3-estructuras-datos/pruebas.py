"""Pruebas con assert para ListaEnlazada y TablaHash."""
import random
 
from estructuras import ListaEnlazada, TablaHash
 
ESTADOS = ["en bodega", "en reparto", "entregado"]
 
 
def prueba_lista() -> None:
    lista = ListaEnlazada()
    for guia, estado in [(1000000010, "en bodega"), (1000000024, "en reparto"),
                         (1000000017, "en bodega"), (1000000005, "entregado")]:
        lista.insertar(guia, estado)
    assert lista.tamano == 4
    assert lista.buscar(1000000024) == "en reparto"   # exitosa
    assert lista.buscar(1000000005) == "entregado"    # exitosa (la primera)
    assert lista.buscar(1999999999) is None           # infructuosa
    assert ListaEnlazada().buscar(5) is None          # lista vacia
 
 
def prueba_tabla() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")
    assert tabla.buscar(24) == "en bodega"            # exitosa
    assert tabla.buscar(99) is None                   # infructuosa
    assert tabla.buscar(3) is None                    # misma casilla, no existe
 
 
def prueba_colision() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, f"estado-{guia}")
    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == f"estado-{guia}"
    assert tabla.casillas[3].tamano == 3
    longitud = 0
    nodo = tabla.casillas[3].cabeza
    while nodo is not None:
        longitud += 1
        nodo = nodo.siguiente
    assert longitud == 3
    assert tabla.factor_carga() == 3 / 7
 
 
def prueba_colecciones_aleatorias() -> None:
    azar = random.Random(123)
    for _ in range(25):
        n = azar.randint(1, 300)
        m = azar.choice([1, 7, 13, 101, 1009])
        guias = azar.sample(range(10**9, 10**10), n)
        lista, tabla = ListaEnlazada(), TablaHash(m)
        for guia in guias:
            estado = azar.choice(ESTADOS)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
        for guia in guias:                            
            assert lista.buscar(guia) == tabla.buscar(guia) is not None
        conjunto = set(guias)
        inexistentes = 0
        while inexistentes < 50:                      
            guia = azar.randint(10**9, 10**10 - 1)
            if guia not in conjunto:
                assert lista.buscar(guia) is None
                assert tabla.buscar(guia) is None
                inexistentes += 1
        assert tabla.factor_carga() == n / m
 
 
if __name__ == "__main__":
    prueba_lista()
    prueba_tabla()
    prueba_colision()
    prueba_colecciones_aleatorias()
    print("Todas las pruebas pasaron.")