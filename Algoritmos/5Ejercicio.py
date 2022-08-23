#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros.
print("Ingrese el numero inicial entero:")
i = int(input())
print("Ingrese el numero final entero: ")
f = int(input())
suma = 0
print("***Los numeros pares entre el rago de enteros son***")

while i <= f:
    if i % 2 == 0:
        print(i)
        suma = suma+i
    i+=1
    print(suma)