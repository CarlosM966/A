"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""

from tokenize import String


print("Ingrese nombre y apellido:")
nombre = input()
print("carrera que desea cursar: ")
carrera = String
print("Ingresa tu promedio: ")
prom = int(input())



# Hacer la comparación
if prom >= 85:
    print("Aprobado")
else:
    print("No aprobado")