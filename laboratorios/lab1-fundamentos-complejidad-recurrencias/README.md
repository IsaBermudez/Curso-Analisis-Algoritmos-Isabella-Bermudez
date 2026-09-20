#### Isabella Bermúdez Arboleda



### Parte 1 — Analizar el algoritmo antes de comprar hardware
Se debe analizar primero el algoritmo porque, aunque hay algoritmos que son correctos, es decir, que cumplen con la función del problema de ordenar por índice de riesgo de mayor a menor, no significa que sea el algoritmo adecuado tras el cambio de las entradas. Pues, pasó de procesar 20.000 registros hace 8 años a 1.200.000 registros en la actualidad.

Por otro lado, duplicar la velocidad del hardware no soluciona el problema de raíz ya que disminuye el tiempo del proceso a la mitad, pero también el problema nos está diciendo que aumentó los registros de hace 8 años 60 veces ahora (60*20.000=1.200.000 registros). Aquí se puede evidenciar la importancia de la elección del algoritmo; si se escoge un algoritmo cuadrático como insertion sort, el trabajo en este caso se multiplicó 60 a la 2 que da 3600 veces más trabajo que hace 8 años. Por tanto, ningún servidor con mejora de velocidad es capaz de compensar el crecimiento cuadrático con la regla de negocio o restricción que nos brinda el problema y es la ventana de cuatro horas (entre las 2:00 am y las 6:00 am) lo cual aunque el algoritmo sea correcto, no es viable.

Un ejemplo concreto es una app de compra de productos y/o comidas de supermercados y restaurantes (tipo Rappi o DidiFood) que utilicé en el quinto semestre para realizar pruebas. Este sistema contaba con alrededor de 100.000 productos registrados, en donde se implementó una búsqueda lineal iterando sobre una lista para filtrar productos por palabras clave. Ahora bien, si su respuesta no era inmediata con un usuario, al tener dos haciendo búsquedas simultáneamente, la latencia superaba los 5 segundos, lo que la hacía menos llamativa y violaba una restricción importante en este tipo de plataformas, en donde debe entregar respuestas en cuestión de pocos milisegundos, pues en estos casos es importante la experiencia del usuario.

### Parte 2 — Responsabilidad ambiental y ética de la implementación
La elección de un algoritmo no solo trae beneficios o consecuencias negativas a nivel de tiempo y rendimiento, sino que también impacta a nivel ambiental y social. Como se dijo anteriormente, una mala elección de un algoritmo hace que el proceso se finalice, pero en cuestión de horas o hasta días. Dicho lo anterior, esto no solo   incumple la restricción del tiempo, sino que también impacta en el consumo energético.
Ahora, si un servidor procesando datos a máxima capacidad consume una potencia constante de 400 W y trabaja alrededor de nueve horas con insertion sort, el consumo sería:

$$Energía\ en\ kWh = \frac{Potencia(Watts) \times tiempo\ de\ ejecución(H)}{1000}$$

$$Consumo\ en\ una\ noche = \frac{400 \times 9}{1000} = 3.6\ kWh$$

$$Consumo\ anual = 3.6\ kWh \times 365 = 1314\ kWh$$

En cambio, con merge sort el proceso puede ejecutarse en cuestión de minutos; por ejemplo, en 10 minutos (0.17 horas):

$$Consumo\ en\ una\ noche = \frac{400 \times 0.17}{1000} = 0.068\ kWh$$

$$Consumo\ anual = 0.068\ kWh \times 365 = 24.82\ kWh$$

La diferencia entre 1314 kWh y 24.82 kWh al año muestra que la elección del algoritmo no es solo una decisión de rendimiento, sino también una decisión con impacto ambiental medible a lo largo del tiempo.

Por lo cual una mala decisión en un algoritmo puede ser un gasto energético innecesario a lo largo de los años y/o durante el ciclo de vida del software. Esto se puede convertir en un verdadero problema ambiental, debido a que la generación de energía puede requerir grandes cantidades de recursos naturales como el agua y producción en exceso de emisiones de carbono.

## ¿Quién paga el costo?
Un actor que puede pagar el costo por una mala decisión de un algoritmo es el paciente con un alto índice de riesgo, el cual si el sistema no termina el proceso con el orden establecido a las 6:00 a.m. será la salud del paciente la que empeore, provocando así agravar la situación o en el peor de los casos la muerte. En la responsabilidad ética juegan dos actores fundamentales. En primer lugar, esta el operador, debido a que no debería realizar su trabajo sabiendo que el insumo que recibió no es el adecuado, ya que estaría trabajando con información que no hace referencia a la realidad de los pacientes. Por ende, existiría un costo o una responsabilidad ética por parte del operador.
Adicionalmente, tenemos otro actor, que es la secretaria, la cual debe asegurarse a que el sistema entregue la lista dentro del rango de tiempo establecido y en el orden adecuado, con el proposito de que el operador reciba el insumo correcto y pueda realizar su labor de manera adecuada.

## ¿Qué obligación adicional impone eso sobre la corrección del ordenamiento, más allá del tiempo?
Aunque el sistema cumpla con su objetivo de ordenar la lista de pacientes, también debe cumplir con uno de los factores fundamentales del problema y es realizar este proceso dentro del rango de tiempo establecido. Si no se completa antes de las 6:00 a. m. la lista que se entrega estará incompleta y no garantizará el orden correcto de prioridad.
Por esta razón, la obligación que tiene el sistema no se limita únicamente a realizar correctamente el ordenamiento, sino también a garantizar que este sea confiable y esté disponible dentro del tiempo establecido. Lo más importante según lo mencionado anteriormente, es que la decisión sobre qué algoritmo utilizar no este condicionada únicamente por solucionar el problema al instante ya que en este caso es importante encontrar un equilibrio entre los diferentes factores con los que el sistema comparte.  De esto depende que los pacientes sean contactados de acuerdo con su nivel de riesgo y que el proceso cumpla con el propósito para el cual fue diseñado.
