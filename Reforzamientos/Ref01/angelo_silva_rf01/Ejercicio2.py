"""
Ejercicio 02. Operaciones y conversiones de tipos de datos
Desarrollar un programa que permita realizar operaciones aritméticas y conversiones utilizando variables de
tipo entero y decimal.
Requisitos:
    1. Crear una variable de tipo int con un valor numérico positivo mayor que 10.
    2. Multiplicar el valor inicial por 10 y almacenar el resultado.
    3. Restar 10 al resultado anterior y almacenarlo en otra variable.
    4. Convertir el resultado final a tipo float.
    5. Dividir el valor convertido entre 3.
    6. Obtener el residuo de la división entre 3 utilizando el operador módulo (%).
    7. Mostrar el valor inicial, los resultados de cada operación, el resultado de la división con dos
    decimales y el tipo de dato de la variable convertida.
"""
num_1=15
mult=num_1*10
rest=mult-10
float_result=float(rest)
div=float_result/3
res=float_result%3

print("------------------------------") 
print("Valor inicial:", num_1)
print("Multiplicación por 10:", mult)
print("Resta de 10:", rest)
print("Conversión a float:", float_result)
print("División entre 3:", round(div, 2))
print("Residuo de la división:", res)   

