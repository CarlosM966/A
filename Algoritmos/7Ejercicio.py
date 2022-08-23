#Leer x cantidad de edades y mostrar el promedio de dichas edades.
n = int(input("ingresa la candidad de edades"))
x = 1
suma = 0
while x <= n:
    edad = int(input("ingresa la edad"))
    suma = suma +  edad
    x += 1
    print("El promedio de edades es:", suma )