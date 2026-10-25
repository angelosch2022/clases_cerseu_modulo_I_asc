"""
Ejercicio 04. Promedio de calificaciones
Desarrollar un programa que calcule el promedio de las calificaciones de un estudiante.
Requisitos:
    1. Crear cinco variables de tipo float que representen las calificaciones de cinco evaluaciones,
    con valores entre 0 y 20.
    2. Calcular la suma de las cinco calificaciones.
    3. Obtener el promedio aritmético.
    4. Calcular la diferencia entre la nota más alta y la más baja.
    5. Utilizar una condicional para determinar si el estudiante está aprobado, considerando una
    nota mínima de 11.
    6. Mostrar las cinco notas, su suma, el promedio con dos decimales, la diferencia y el estado
    final.
Ejemplo esperado:
    Notas: 15.5, 17.0, 12.5, 18.0, 14.0
    Suma de notas: 77.0
    Promedio: 15.40
    Diferencia entre nota mayor y menor: 5.50
    Estado: APROBADO
"""
cal_01=18.5
cal_02=17.0
cal_03=12.5
cal_04=0
cal_05=0
suma=cal_01 + cal_02 + cal_03 + cal_04 + cal_05
diferencia_maxmin=max(cal_01, cal_02, cal_03, cal_04, cal_05) - min(cal_01, cal_02, cal_03, cal_04, cal_05)
promedio=suma/5
if promedio >= 11:
    estado="APROBADO"
else:
    estado="DESAPROBADO"
print("Sus notas son:{}, {}, {}, {}, {}".format(cal_01, cal_02, cal_03, cal_04, cal_05))
print("La suma de sus notas es: {}".format(suma))
print("El promedio de sus notas es: {:.2f}".format(promedio))
print("La diferencia entre la nota mayor y menor es: {:.2f}".format(diferencia_maxmin))
print("El estado final es: {}".format(estado))  