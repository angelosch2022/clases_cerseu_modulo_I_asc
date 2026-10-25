"""
Requisitos:
  1. Crear 4 variables, entre enteros, booleans, strings
  2. Realizar el uso de condincionales de las variables, para 2 casos true y 2 casos false
  3. En casos que valide True, imprimir el valor de las dos variables
  4. En dos condicionales comparar variables (< o >)
"""
numero = 100
esEntero= True
esValido = False
pais = "Perú"

if numero>0:
    print("Mi número {} es positivo y {}".format(numero, esEntero))

if esEntero:
    print("El valor de la variable {} es {}".format(numero, esEntero))

if pais == "España":
    print("El país ingresado es {}".format(pais))

if esEntero < esValido:
    print("El valor de la variable es {}".format(esValido))

