"""Verificacion de los algoritmos para encontrar la mejor racha."""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


def comparar_algoritmos(datos: list[float]) -> None:
    """Verifica que los algoritmos encuentren la misma suma maxima.

    Args:
        datos: Lista de variaciones diarias que se van a evaluar.
    """
    datos_originales = datos.copy()

    resultado_bruto = subarreglo_fuerza_bruta(datos)
    resultado_recursivo = subarreglo_maximo(
        datos, 0, len(datos) - 1
    )

    assert resultado_bruto[2] == resultado_recursivo[2], (
        f"Las sumas no coinciden para {datos}: "
        f"{resultado_bruto[2]} y {resultado_recursivo[2]}"
    )

    assert datos == datos_originales, (
        "Los algoritmos modificaron la lista recibida."
    )


def probar_casos_conocidos() -> None:
    """Comprueba los casos de prueba definidos para el laboratorio."""
    # Caso empresarial: la mejor racha suma 17.
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(
        serie, 0, len(serie) - 1
    )[2] == 17

    comparar_algoritmos(serie)

    # Caso con un solo dia.
    un_dia = [-4]
    comparar_algoritmos(un_dia)
    assert subarreglo_maximo(un_dia, 0, 0)[2] == -4

    # Todos los dias tienen variaciones negativas.
    perdidas = [-10, -4, -7, -2, -9]
    comparar_algoritmos(perdidas)
    assert subarreglo_fuerza_bruta(perdidas)[2] == -2
    assert subarreglo_maximo(
        perdidas, 0, len(perdidas) - 1
    )[2] == -2

    # Todos los dias tienen variaciones positivas.
    ganancias = [3, 6, 2, 5]
    comparar_algoritmos(ganancias)
    assert subarreglo_fuerza_bruta(ganancias)[2] == 16
    assert subarreglo_maximo(
        ganancias, 0, len(ganancias) - 1
    )[2] == 16

    # La mejor racha atraviesa el punto medio.
    racha_cruzada = [3, -2, 5, -1, 4, -6]
    comparar_algoritmos(racha_cruzada)

    assert subarreglo_maximo(
        racha_cruzada, 0, len(racha_cruzada) - 1
    )[2] == 9


def probar_listas_aleatorias() -> None:
    """Compara ambos algoritmos con veinte listas aleatorias."""
    generador = random.Random(123)

    for numero_prueba in range(20):
        longitud = generador.randint(1, 25)

        variaciones = [
            generador.randint(-15, 15)
            for _ in range(longitud)
        ]

        comparar_algoritmos(variaciones)


if __name__ == "__main__":
    probar_casos_conocidos()
    probar_listas_aleatorias()

    print("Todas las pruebas pasaron correctamente.")