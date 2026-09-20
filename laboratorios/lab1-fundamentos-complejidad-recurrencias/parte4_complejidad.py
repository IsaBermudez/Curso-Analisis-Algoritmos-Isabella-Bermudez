"""Comparacion experimental de Insertion Sort y Merge Sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


tamaño_prueba = [100, 200, 400, 800, 1600, 3200, 6400]
semilla_datos = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def medir_tiempo(funcion, entrada):
    """Mide cuanto tarda una funcion en procesar una entrada.

    Args:
        funcion: funcion de ordenamiento a medir (insertion_sort o
            merge_sort).
        entrada: lista de indices de riesgo a ordenar.

    Returns:
        El tiempo en segundos que tardo la funcion en procesar la
        entrada.
    """

    inicio = time.perf_counter()
    funcion(entrada)
    fin = time.perf_counter()

    return fin - inicio


def realizar_pruebas():
    """Mide insertion sort y merge sort sobre el escenario A de Tamiza.

    Para cada tamano de tamaño_prueba genera un lote aleatorio con
    generar_aleatorio y mide, sobre ese mismo lote, el tiempo de
    ejecucion de insertion_sort y de merge_sort.

    Returns:
        Una tupla con dos listas: los tiempos de insertion sort y los
        tiempos de merge sort, en el mismo orden que tamaño_prueba.
    """

    tiempos_insertion = []
    tiempos_merge = []

    for cantidad in tamaño_prueba:
        datos = generar_aleatorio(cantidad, semilla_datos)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos,
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

    return tiempos_insertion, tiempos_merge


def crear_grafica(tiempos_insertion, tiempos_merge):
    """Crea la grafica comparativa de tiempos.

    Guarda el archivo en graficas/parte4_tiempo.png.

    Args:
        tiempos_insertion: tiempos de insertion sort, en el mismo
            orden que tamaño_prueba.
        tiempos_merge: tiempos de merge sort, en el mismo orden que
            tamaño_prueba.
    """

    plt.plot(
        tamaño_prueba,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        tamaño_prueba,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución: Insertion Sort vs Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    insertion, merge = realizar_pruebas()

    print("\nInsertion Sort")
    print("Tiempo:", insertion)

    print("\nMerge Sort")
    print("Tiempo:", merge)

    crear_grafica(insertion, merge)