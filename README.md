Amelia Maldonado Carrillo

Descripción: Es un algoritmo de ordenamiento en el que se comparan pares de elementos que están uno junto al otro y los intercambia de posición si el orden está erróneo.

Complejidad Computacional: 

1. Tiene complejidad Big O = O(n^2)
2. En base a los 2 ciclos anidados for que existen dentro del programa. En el peor de los casos, se multiplica el rango del primer for por el rango del segundo for para hacer un ordenamiento. 
   Porque, va a tomar todo el recorrido de las dos listas para ordenar el array (por cada elemento del bucle externo, se debe recorrer nuevamente la lista para realizar comparaciones 
   (bucle interno).
3. Al tener 10 elementos, el máximo de operaciones estimadas es (10 * 10) = 100 operaciones. Por otro lado, al tener 100 elementos, el máximo es (100 * 100) = 10 000 operaciones máximas.
   Esto significa que al tener que ordenar 100 elementos, toma 10 veces más el tiempo que solo 10 elementos. 
 
