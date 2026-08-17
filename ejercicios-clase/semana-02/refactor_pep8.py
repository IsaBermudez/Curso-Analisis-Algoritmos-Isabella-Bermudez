def calcular_promedio(lista: list[int]) -> float:
    """
    Calcula el promedio de una lista de números enteros.

    Args: lista (list[int]): Una lista de números enteros.

    Returns: float: El promedio de los números en la lista.
    """
    total = 0
    for x in lista:
        total += x

    return total/len(lista)

def main() -> None:
    """Ejecuta el programa principal"""
    numeros=[1,2,3,4,5]
    promedio=calcular_promedio(numeros)
    print(promedio)

if __name__ == "__main__":
    main()