"""
Ejercicio 03. Conversión de cadenas y operaciones numéricas
Crear un programa en Python que permita realizar operaciones entre valores almacenados inicialmente con
distintos tipos de datos.
Requisitos:
    1. Crear una variable de tipo str que contenga un número entero positivo, por ejemplo "35".
    2. Crear una segunda variable de tipo int con otro valor numérico, por ejemplo 15.
    3. Convertir la primera variable al tipo de dato correspondiente para realizar operaciones aritméticas
    sin errores.
    4. Calcular la suma y la multiplicación de ambos valores.
    5. Obtener el promedio de los dos números y mostrarlo con dos decimales.
    6. Convertir el resultado de la suma a tipo str y concatenarlo con el mensaje "El resultado final es: ".
    7. Mostrar los resultados de todas las operaciones y el tipo de dato obtenido en la conversión inicial.
"""
num_str="26"
num_int= 18
num_str_int=int(num_str)
sum= num_int + num_str_int
mult=num_int*num_str_int
prom = (num_int+num_str_int)/2
sum_str=str(sum)
print("----------------------------------")
print("Valor inicial de tipo string:", num_str)
print("Valor inicial de tipo entero:", num_int)
print("Suma de ambos valores:", sum)
print("Multiplicación de ambos valores:", mult)
print("Promedio de ambos valores:", round(prom,2))
print("El resultado final es: "+sum_str)