""" 
Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9). """

def suma_cuadrados(*variables):
    
    total = 0
    
    for multi in variables:
        cuadrado = multi ** 2
        total += cuadrado
    return (total)


resultado = suma_cuadrados(1,2,3)
print(resultado)

