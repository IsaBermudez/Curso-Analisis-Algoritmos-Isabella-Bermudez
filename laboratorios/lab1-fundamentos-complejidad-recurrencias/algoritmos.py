"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia_datos = datos.copy()
    comparaciones = 0

    for i in range(1, len(copia_datos)):
        clave = copia_datos[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if copia_datos[j] >= clave:
                break

            copia_datos[j + 1] = copia_datos[j]
            j -= 1

        copia_datos[j + 1] = clave

    return copia_datos, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    elementos = datos.copy()

    def dividir_y_ordenar(valores):
        if len(valores) <= 1:
            return valores, 0

        punto_medio = len(valores) // 2

        izquierda, comp_izquierda = dividir_y_ordenar(
            valores[:punto_medio]
        )
        derecha, comp_derecha = dividir_y_ordenar(
            valores[punto_medio:]
        )

        combinados = []
        indice_izq = 0
        indice_der = 0
        total_comparaciones = comp_izquierda + comp_derecha

        while (
            indice_izq < len(izquierda)
            and indice_der < len(derecha)
        ):
            total_comparaciones += 1

            if izquierda[indice_izq] >= derecha[indice_der]:
                combinados.append(izquierda[indice_izq])
                indice_izq += 1
            else:
                combinados.append(derecha[indice_der])
                indice_der += 1

        if indice_izq < len(izquierda):
            combinados.extend(izquierda[indice_izq:])

        if indice_der < len(derecha):
            combinados.extend(derecha[indice_der:])

        return combinados, total_comparaciones

    return dividir_y_ordenar(elementos)
