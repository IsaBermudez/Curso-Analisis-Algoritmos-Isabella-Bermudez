"""Experimento de los tres escenarios de Tamiza para el Laboratorio 1."""

import time
from pathlib import Path

from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


tamaños = [100, 200, 400, 800, 1600, 3200, 6400]
semilla = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def ejecutar():
    """Ejecuta insertion sort sobre los tres escenarios de Tamiza.

    Para cada tamaño (tamaños) genera un lote con cada uno de los
    generadores de escenarios (A, B y C) y mide, sobre ese lote, el
    tiempo de ejecucion y el numero de comparaciones de
    insertion_sort.

    Returns:
        Diccionario con una entrada por escenario, donde cada valor
        es a su vez un diccionario con las listas "tiempo" y
        "comparaciones" registradas para cada tamaño de tamaños.
    """

    resultados = {
        "A - Aleatorio": {"tiempo": [], "comparaciones": []},
        "B - Casi ordenado": {"tiempo": [], "comparaciones": []},
        "C - Inverso": {"tiempo": [], "comparaciones": []},
    }

    for n in tamaños:
        datos_a = generar_aleatorio(n, semilla)
        datos_b = generar_casi_ordenado(n, semilla)
        datos_c = generar_inverso(n)

        escenarios = [
            ("A - Aleatorio", datos_a),
            ("B - Casi ordenado", datos_b),
            ("C - Inverso", datos_c),
        ]

        for nombre, datos in escenarios:
            inicio = time.perf_counter()
            _, comparaciones = insertion_sort(datos)
            fin = time.perf_counter()

            resultados[nombre]["tiempo"].append(fin - inicio)
            resultados[nombre]["comparaciones"].append(comparaciones)

    return resultados
def generar_grafica_comparaciones(resultados):
    """Genera la grafica de comparaciones contra tamaño de entrada.

    Guarda el archivo en graficas/parte3_comparaciones.png.

    Args:
        resultados: diccionario con el mismo formato que retorna
            ejecutar(), con las comparaciones por escenario.
    """

    for nombre, datos in resultados.items():
        plt.plot(
            tamaños,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.title("Insertion Sort: comparaciones por escenario")

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_comparaciones.png")
    plt.close()


def generar_grafica_tiempo(resultados):
    """Genera la grafica de tiempo contra tamaño de entrada.

    Guarda el archivo en graficas/parte3_tiempo.png.

    Args:
        resultados: diccionario con el mismo formato que retorna
            ejecutar(), con los tiempos por escenario.
    """

    for nombre, datos in resultados.items():
        plt.plot(
            tamaños,
            datos["tiempo"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (seg)")
    plt.title("Insertion Sort: tiempo de ejecución por escenario")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    resultados = ejecutar()

    for nombre, datos in resultados.items():
        print(f"\n{nombre}")
        print("Comparaciones:", datos["comparaciones"])
        print("Tiempo:", datos["tiempo"])

    generar_grafica_comparaciones(resultados)
    generar_grafica_tiempo(resultados)