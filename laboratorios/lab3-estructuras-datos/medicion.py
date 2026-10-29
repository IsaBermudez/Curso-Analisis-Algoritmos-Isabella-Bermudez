"""Experimentos A y B: lista enlazada frente a tabla hash."""
import os
import random
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from estructuras import ListaEnlazada, TablaHash  # noqa: E402

SEMILLA_GUIAS = 42
BUSQUEDAS = 200
REPETICIONES = 3
CARPETA = os.path.dirname(os.path.abspath(__file__))
CARPETA_GRAFICAS = os.path.join(CARPETA, "graficas")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor, desde el objetivo hacia arriba.

    Args:
        objetivo: valor de referencia.

    Returns:
        El menor primo mayor o igual que el objetivo.
    """
    candidato = max(objetivo, 2)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def generar_guias(n: int, semilla: int = SEMILLA_GUIAS) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    return random.Random(semilla).sample(range(10**9, 10**10), n)


def construir(guias: list[int], m: int) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias.

    Args:
        guias: guias a insertar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya pobladas.
    """
    azar = random.Random(1)
    estados = ["en bodega", "en reparto", "entregado"]
    lista, tabla = ListaEnlazada(), TablaHash(m)
    for guia in guias:
        estado = azar.choice(estados)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(lista: ListaEnlazada, tabla: TablaHash,
              guias: list[int]) -> None:
    """Comprueba que lista y tabla dan el mismo estado en una muestra.

    Args:
        lista: lista enlazada poblada.
        tabla: tabla hash poblada.
        guias: guias existentes de las que se toma la muestra.
    """
    muestra = random.Random(5).sample(guias, min(200, len(guias)))
    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia) is not None


def tiempo_medio(estructura: ListaEnlazada | TablaHash,
                 busquedas: list[int]) -> float:
    """Mide el tiempo medio por busqueda, promediando varias repeticiones.

    Solo se cronometran las busquedas.

    Args:
        estructura: lista o tabla donde buscar.
        busquedas: guias a buscar.

    Returns:
        Tiempo medio por busqueda en microsegundos.
    """
    medias = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in busquedas:
            estructura.buscar(guia)
        total = time.perf_counter() - inicio
        medias.append(total / len(busquedas))
    return sum(medias) / len(medias) * 1e6


def experimento_a() -> None:
    """Mide lista frente a tabla (m primo cercano a n/2) y grafica."""
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    t_lista, t_tabla = [], []
    print("Experimento A (busquedas infructuosas, us/busqueda)")
    print(f"{'n':>7} {'m':>7} {'alfa':>6} {'lista':>12} {'tabla':>10}")
    for n in valores_n:
        guias = generar_guias(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        busquedas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        tl = tiempo_medio(lista, busquedas)
        tt = tiempo_medio(tabla, busquedas)
        t_lista.append(tl)
        t_tabla.append(tt)
        print(f"{n:>7} {m:>7} {tabla.factor_carga():>6.2f} "
              f"{tl:>12.2f} {tt:>10.3f}")

    plt.figure(figsize=(7, 4.5))
    plt.plot(valores_n, t_lista, "o-", label="Lista enlazada")
    plt.plot(valores_n, t_tabla, "s-", label="Tabla hash (alfa ~ 2)")
    plt.title("Busqueda de guias inexistentes: lista vs tabla hash")
    plt.xlabel("Numero de guias n (envios)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"), dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga con n fijo y grafica."""
    n = 20000
    alfas_objetivo = [0.25, 0.5, 1, 2, 4, 10]
    guias = generar_guias(n)
    busquedas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    alfas, tiempos = [], []
    print("\nExperimento B (n = 20000, us/busqueda)")
    print(f"{'alfa obj':>9} {'m':>7} {'alfa real':>10} {'tabla':>10}")
    for objetivo in alfas_objetivo:
        m = primo_cercano(round(n / objetivo))
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        t = tiempo_medio(tabla, busquedas)
        alfas.append(tabla.factor_carga())
        tiempos.append(t)
        print(f"{objetivo:>9} {m:>7} {tabla.factor_carga():>10.3f} {t:>10.3f}")

    plt.figure(figsize=(7, 4.5))
    plt.plot(alfas, tiempos, "o-", label="Tabla hash, n = 20.000")
    plt.title("Efecto del factor de carga en la busqueda")
    plt.xlabel("Factor de carga alfa = n / m (guias por casilla)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png"), dpi=150)
    plt.close()


if __name__ == "__main__":
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    experimento_a()
    experimento_b()