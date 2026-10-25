"""
Ejercicio intervención
"""

"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesion y ciudad
2. Crear dos varaibles para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 varibles donde se sumará el ingreso de los dos meses: enero y febrero
4. Mostrar en pantalla el siguiente mensaje (Output)

"Hola soy 'nombre', soy 'profesión' y mi remuneración acumulada es de ''remunera_total"

rem_1
remunera_1
rem_enero

"""
nombre_1="Juan"
nombre_2="Pedro"
profesion_1="Ingeniero"
profesion_2="Arquitecto"
ciuda_1="Lima"
ciudad_2="Arequipa"

rem1_enero=1600
rem1_febrero=2510

rem2_enero=1800
rem2_febrero=3000

suma_rem1=rem1_enero+rem1_febrero
suma_rem2=rem2_enero+rem2_febrero

print("Hola soy {}, soy {} y mi remuneración acumulada es de {}".format(nombre_1,profesion_1,suma_rem1))
print("Hola soy {}, soy {} y mi remuneración acumulada es de {}".format(nombre_2,profesion_2,suma_rem2))
