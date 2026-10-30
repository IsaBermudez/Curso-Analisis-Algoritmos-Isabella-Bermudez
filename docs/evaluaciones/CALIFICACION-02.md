# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Isabella Bermúdez Arboleda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `0856c3b`

Muy buen trabajo: el laboratorio está completo, ordenado y bien sustentado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre 10 y 50 elementos y explica por qué las llamadas recursivas pesan en listas pequeñas.
- En el máximo de un arreglo plantea `T(n) = 2T(n/2) + Θ(1)`, concluye `Θ(n)` y explica que dividir no mejora nada.
- La estimación a un millón de registros está declarada como estimación y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 4 podría decir con más claridad que dividir no gana porque combinar cuesta lo mismo que comparar dos números, y que además agrega el costo de las llamadas.
- En la pregunta 5 faltó mencionar que la estimación ignora efectos como la memoria o la profundidad de la recursión con tantos datos.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica los dos subproblemas y el costo del caso cruzado.
- Resuelve con el método maestro y comprueba que `f(n) = Θ(n)` coincide con `n^(log₂ 2)`, así que aplica el caso 2.
- Justifica el `Θ(n²)` de la fuerza bruta con los dos ciclos anidados.

**Lo que puede mejorar:**
- Falta mostrar un paso más: por qué el barrido del caso cruzado recorre cada elemento una sola vez.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y no modifica la lista recibida.
- Tiene *type hints*, *docstrings* y el código cumple PEP 8.

**Lo que puede mejorar:**
- Las 20 listas aleatorias de `pruebas.py` son cortas (hasta 25 elementos); con listas más largas las pruebas serían más exigentes.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calcula los factores al duplicar `n` (3,89 y 2,0 de 50 a 100; 3,13 y 1,81 de 4000 a 8000) y los compara con lo esperado.
- Incluye una tabla con los valores medidos y repite cada medición tres veces.

**Lo que puede mejorar:**
- El factor de 3,13 para la fuerza bruta se aleja de 4 y la explicación ("variaciones normales") es muy general; podría relacionarlo con el ruido de medir pocas repeticiones.
- Varias afirmaciones salen de la tabla; conviene apoyarlas también en lo que se lee en la gráfica.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` tiene todos los archivos pedidos y la gráfica se ve en el informe.
- Enlaza `subarreglo.py`, `pruebas.py` y `medicion.py`, incluye instrucciones de reproducción y tiene cuatro commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma en cientos de listas aleatorias y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Pruebe con listas más largas, además de las cortas.
- Apoye cada afirmación de desempeño en valores leídos de la gráfica y, cuando un factor no coincida con la teoría, busque una causa concreta.
- Al estimar tiempos grandes, mencione qué limitaciones tiene la estimación.
