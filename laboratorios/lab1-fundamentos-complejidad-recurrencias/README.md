## Isabella Bermúdez Arboleda



## Parte 1 — Analizar el algoritmo antes de comprar hardware
Se debe analizar primero el algoritmo porque, aunque hay algoritmos que son correctos, es decir, que cumplen con la función del problema de ordenar por índice de riesgo de mayor a menor, no significa que sea el algoritmo adecuado tras el cambio de las entradas. Pues, pasó de procesar 20.000 registros hace 8 años a 1.200.000 registros en la actualidad.

Por otro lado, duplicar la velocidad del hardware no soluciona el problema de raíz ya que disminuye el tiempo del proceso a la mitad, pero también el problema nos está diciendo que aumentó los registros de hace 8 años 60 veces ahora (60*20.000=1.200.000 registros). Aquí se puede evidenciar la importancia de la elección del algoritmo; si se escoge un algoritmo cuadrático como insertion sort, el trabajo en este caso se multiplicó 60 a la 2 que da 3600 veces más trabajo que hace 8 años. Por tanto, ningún servidor con mejora de velocidad es capaz de compensar el crecimiento cuadrático con la regla de negocio o restricción que nos brinda el problema y es la ventana de cuatro horas (entre las 2:00 am y las 6:00 am) lo cual aunque el algoritmo sea correcto, no es viable.

Un ejemplo concreto es una app de compra de productos y/o comidas de supermercados y restaurantes (tipo Rappi o DidiFood) que utilicé en el quinto semestre para realizar pruebas. Este sistema contaba con alrededor de 100.000 productos registrados, en donde se implementó una búsqueda lineal iterando sobre una lista para filtrar productos por palabras clave. Ahora bien, si su respuesta no era inmediata con un usuario, al tener dos haciendo búsquedas simultáneamente, la latencia superaba los 5 segundos, lo que la hacía menos llamativa y violaba una restricción importante en este tipo de plataformas, en donde debe entregar respuestas en cuestión de pocos milisegundos, pues en estos casos es importante la experiencia del usuario.

