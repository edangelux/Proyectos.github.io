""" 
Práctica Rango 3
Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.

Para ello:

Crea un rango de valores que puedas recorrer en un loop

Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).

Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados. """
suma_cuadrados = 0
for i in range(1, 16):
    cuadrado = i ** 2
    suma_cuadrados += cuadrado
print(suma_cuadrados)
    