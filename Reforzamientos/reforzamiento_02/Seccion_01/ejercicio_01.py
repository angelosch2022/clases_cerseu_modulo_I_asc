"""
Ejercicio 01. Manipulación de cadenas de texto
Crear un programa en Python que almacene los datos personales de un estudiante y genere un mensaje
de presentación.
Requisitos:
    1. Crear tres variables para almacenar el nombre, apellido paterno y apellido materno de un
    estudiante.
    2. Crear una variable llamada nombre_completo que concatene los tres datos anteriores,
    incluyendo los espacios correspondientes.
    3. Crear una variable llamada mi_saludo, cuyo contenido sea: ¡HI Nombre ApellidoPaterno
    ApellidoMaterno!.
    4. Obtener la cantidad total de caracteres del nombre completo, incluyendo los espacios.
    5. Mostrar el saludo, el nombre completo en mayúsculas y la cantidad de caracteres.
Ejemplo esperado:
    Saludo: ¡HI Luis Gamarra Torres!
    Nombre completo: LUIS GAMARRA TORRES
    Cantidad de caracteres: 19
"""
nombre="Angelo"
apellido_paterno="Silva"
apellido_materno="Chiroque"
nombre_completo=nombre + " " + apellido_paterno + " " + apellido_materno
mi_saludo=f"¡HI {nombre} {apellido_paterno} {apellido_materno}!"
num_caracteres = len(nombre_completo)
print("Saludo: {}".format(mi_saludo))
print("Nombre completo: {}".format(nombre_completo.upper()))
print("Cantidad de caracteres: {}".format(num_caracteres))