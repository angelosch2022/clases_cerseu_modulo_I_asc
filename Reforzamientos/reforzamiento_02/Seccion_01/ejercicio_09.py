"""
Ejercicio 09. Cálculo del Índice de Masa Corporal (IMC)
Desarrollar un programa que permita calcular el Índice de Masa Corporal de una persona y
determinar su clasificación.
Requisitos:
    1. Crear variables para almacenar el nombre, peso en kilogramos y estatura en metros de una
    persona.
    2. Calcular el IMC utilizando la fórmula: IMC = peso / (estatura ** 2).
    3. Determinar su clasificación utilizando condicionales:
        o Menor de 18.5: Bajo peso.
        o Desde 18.5 hasta menos de 25: Peso normal.
        o Desde 25 hasta menos de 30: Sobrepeso.
        o Desde 30 en adelante: Obesidad.
    4. Mostrar el nombre de la persona, peso, estatura, IMC con dos decimales y clasificación obtenida.

Ejemplo esperado:
    Nombre: Carlos Torres
    Peso: 72.0 kg
    Estatura: 1.75 m
    IMC calculado: 23.51
    Clasificación: Peso normal
"""
nombre = "Angelo Silva"
peso = 77
estatura = 1.74
imc = peso / (estatura ** 2)
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print("Nombre: {}".format(nombre))
print("Peso: {} kg".format(peso))
print("Estatura: {} m".format(estatura))
print("IMC calculado: {:.2f}".format(imc))
print("Clasificación: {}".format(clasificacion))
