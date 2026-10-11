# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Isabella Bermúdez Arboleda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `9b9e247`

Muy buen trabajo: el laboratorio está completo, ordenado y su código funciona.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **81 / 100** |
| **Nota (0–5)** | **4.05** |

## 1. Corrección conceptual (20 / 25)
**Lo que hizo bien:**
- Explica que el algoritmo es correcto pero no cabe en la ventana de cuatro horas, y por qué duplicar el servidor no basta (60 veces más datos son 3600 veces más trabajo con un algoritmo cuadrático).
- Su ejemplo propio (app de productos con 100.000 registros y respuestas de más de 5 segundos) tiene datos y una restricción clara.
- El cálculo de energía por noche y por año (1314 kWh frente a 24,82 kWh) muestra bien el efecto de repetir el proceso todos los días.
- Identifica al paciente como quien más pierde.

**Lo que puede mejorar:**
- Distinga con más claridad "da el resultado correcto" de "lo da a tiempo" al inicio de la Parte 1.
- En la Parte 2 el papel del operador y de la Secretaría queda confuso: diga con precisión quién asume el costo de cada perjuicio.
- La pregunta sobre la obligación adicional (el orden decide a quién se llama primero) quedó respondida con ideas de tiempo. Faltó decir que un error en el orden puede dejar sin llamar a tiempo a quien más lo necesita.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define los tres casos, justifica que usaría el peor caso para decidir si entra en producción y deja la predicción escrita antes de medir.
- Resuelve la recurrencia de merge sort con el método maestro, identifica `a`, `b` y `f(n)` y verifica la condición del caso 2.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- En el caso promedio, diga sobre qué conjunto de entradas se promedia.
- El cálculo línea a línea de insertion sort lista cuántas veces se ejecuta cada línea, pero no suma esos costos ni llega a una expresión final. Además solo se hace para el peor caso.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien en los tres escenarios, no cambian la lista original, cuentan comparaciones entre elementos y no usan `sorted()` ni `.sort()`.
- Los generadores devuelven valores distintos, del tamaño pedido y con semilla.
- El código no tiene problemas de estilo PEP 8.

**Lo que puede mejorar:**
- Faltan *type hints* en las funciones de `parte3_casos.py` y `parte4_complejidad.py` (`ejecutar`, `generar_grafica_comparaciones`, `medir_tiempo`, etc.) y en la función interna de `merge_sort`.
- La función interna de `merge_sort` no tiene *docstring*.
- Algunos *docstrings* no siguen del todo el formato Google (secciones `Args` y `Returns` completas).

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el más cercano al promedio (A), y compara con su predicción.
- La recomendación de merge sort está bien razonada. Hace la extrapolación a 1.200.000 registros (unas 21,9 horas para insertion sort y unos 12 segundos para merge sort), dice que es una estimación, responde a la propuesta del servidor y menciona la memoria extra.

**Lo que puede mejorar:**
- Los números del informe (por ejemplo, 4,13 s del escenario C y 2,24 s de insertion sort con n = 6400) no coinciden con lo que muestran las gráficas publicadas (cerca de 2,4 s y 1,3 s). Revise que el texto cite lo que se ve en su propia gráfica.
- Reconoce que B no es el mejor caso teórico, pero no explica qué lo haría, ni que la lista ya ordenada daría `n - 1` comparaciones.
- Las gráficas de tiempo no aclaran cómo se midió (una sola corrida). Repetir y promediar daría curvas más confiables.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El laboratorio está en una carpeta válida, con los archivos y gráficas del entregable.
- El informe tiene su nombre, instrucciones de reproducción, las partes en orden, las gráficas visibles y los enlaces al código.
- Hay más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de activación del entorno solo cubren PowerShell.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan bien y se generan las gráficas.

## Para el próximo laboratorio
- Agregue *type hints* y *docstrings* a todas las funciones, incluidas las internas.
- Después de generar las gráficas, copie al informe los números que realmente aparecen en ellas.
- En los análisis teóricos, muestre la suma final de costos y cubra también el mejor caso.
- Al hablar de impacto en personas, diga con precisión quién asume cada costo.
- Repita las mediciones de tiempo y promedie para tener curvas más estables.
