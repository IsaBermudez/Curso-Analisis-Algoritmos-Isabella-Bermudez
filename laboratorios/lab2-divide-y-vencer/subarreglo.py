"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias.

    Args:
        valores: Variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    inicio_mejor = 0
    final_mejor = 0
    suma_mejor = float("-inf")

    for inicio in range(len(valores)):
        acumulado = 0

        for ultimo in range(inicio, len(valores)):
            acumulado += valores[ultimo]

            if acumulado > suma_mejor:
                suma_mejor = acumulado
                inicio_mejor = inicio
                final_mejor = ultimo

    return inicio_mejor, final_mejor, suma_mejor


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango considerado (inclusive).
        medio: Indice del ultimo elemento de la mitad izquierda.
        fin: Indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    mejor_suma_izquierda = float("-inf")
    acumulado = 0
    posicion_inicial = medio

    for posicion in range(medio, inicio - 1, -1):
        acumulado += valores[posicion]

        if acumulado > mejor_suma_izquierda:
            mejor_suma_izquierda = acumulado
            posicion_inicial = posicion

    mejor_suma_derecha = float("-inf")
    acumulado = 0
    posicion_final = medio + 1

    for posicion in range(medio + 1, fin + 1):
        acumulado += valores[posicion]

        if acumulado > mejor_suma_derecha:
            mejor_suma_derecha = acumulado
            posicion_final = posicion

    suma_combinada = mejor_suma_izquierda + mejor_suma_derecha

    return posicion_inicial, posicion_final, suma_combinada


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango a considerar (inclusive).
        fin: Indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    punto_medio = (inicio + fin) // 2

    resultado_izquierdo = subarreglo_maximo(
        valores, inicio, punto_medio
    )
    resultado_derecho = subarreglo_maximo(
        valores, punto_medio + 1, fin
    )
    resultado_cruzado = suma_cruzada(
        valores, inicio, punto_medio, fin
    )

    resultado_mejor = resultado_izquierdo

    if resultado_derecho[2] > resultado_mejor[2]:
        resultado_mejor = resultado_derecho

    if resultado_cruzado[2] > resultado_mejor[2]:
        resultado_mejor = resultado_cruzado

    return resultado_mejor