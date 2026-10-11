"""Medicion y comparacion de tiempos de los algoritmos."""

import random
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


def medir_tiempo(
    algoritmo: Callable[[list[int]], tuple[int, int, float]],
    datos: list[int],
) -> float:
    """Calcula el tiempo promedio de ejecucion de un algoritmo.

    Args:
        algoritmo: Funcion que se desea medir.
        datos: Lista de variaciones que recibira el algoritmo.

    Returns:
        Tiempo promedio de ejecucion en segundos.
    """
    cantidad_repeticiones = 3
    duraciones = []

    for _ in range(cantidad_repeticiones):
        momento_inicial = time.perf_counter()
        algoritmo(datos)
        momento_final = time.perf_counter()

        duraciones.append(momento_final - momento_inicial)

    return sum(duraciones) / cantidad_repeticiones


def ejecutar_mediciones() -> None:
    """Compara los tiempos y crea la grafica del experimento."""
    lista_tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    generador_aleatorio = random.Random(2026)

    resultados_bruta = []
    resultados_recursivos = []

    for n in lista_tamanos:
        # Preparar una lista reproducible para ambos algoritmos.
        variaciones = [
            generador_aleatorio.randint(-100, 100)
            for _ in range(n)
        ]

        # La funcion medida recibe la misma lista en ambos casos.
        tiempo_bruta = medir_tiempo(
            subarreglo_fuerza_bruta, variaciones
        )

        tiempo_recursivo = medir_tiempo(
            lambda datos: subarreglo_maximo(
                datos, 0, len(datos) - 1
            ),
            variaciones,
        )

        # Validar las sumas maximas fuera de la medicion.
        suma_bruta = subarreglo_fuerza_bruta(variaciones)[2]
        suma_recursiva = subarreglo_maximo(
            variaciones, 0, len(variaciones) - 1
        )[2]

        assert suma_bruta == suma_recursiva, (
            f"Error en n={n}: las sumas maximas son diferentes."
        )

        resultados_bruta.append(tiempo_bruta)
        resultados_recursivos.append(tiempo_recursivo)

        print(
            f"Elementos: {n} | "
            f"Fuerza bruta: {tiempo_bruta:.6f} s | "
            f"Divide y venceras: {tiempo_recursivo:.6f} s"
        )

    carpeta_graficas = Path(__file__).parent / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        lista_tamanos,
        resultados_bruta,
        marker="o",
        label="Fuerza bruta",
    )
    plt.plot(
        lista_tamanos,
        resultados_recursivos,
        marker="s",
        label="Divide y venceras",
    )

    plt.title("Comparacion de tiempos de ejecucion")
    plt.xlabel("Tamano de entrada (n elementos)")
    plt.ylabel("Tiempo promedio de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(carpeta_graficas / "tiempo_vs_n.png", dpi=150)
    plt.close()

    print("\nMediciones finalizadas correctamente.")
    print("Archivo generado: graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    ejecutar_mediciones()