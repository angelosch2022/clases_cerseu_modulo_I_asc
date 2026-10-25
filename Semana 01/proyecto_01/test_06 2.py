"""
Requisitos:
  1. Crear 4 variables, entre enteros, booleans, strings
  2. Realizar el uso de condincionales de las variables, para 2 casos true y 2 casos false
  3. En casos que valide True, imprimir el valor de las dos variables
  4. En dos condicionales comparar variables (< o >)
"""
numero = 100
EsEntero= True
EsValido = False
Pais = "Perú"

if numero>0:
    print("El número {} es positivo".format(numero))

if EsEntero:
    print("El valor de la variable es {}".format(EsEntero))

if Pais == "España":
    print("El país ingresado es {}".format(Pais))

if EsEntero < EsValido:
    print("El valor de la variable es {}".format(EsValido))

