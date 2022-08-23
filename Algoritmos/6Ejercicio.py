#Leer dos números y decir cual es mayor y cual es menor.

print("Ingresa dos numeros: ")
print("Ingresa el primer numero: ")
n1 = int(input())
print("Ingresa el segundo numero: ")
n2 = int(input())

if n1<n2:
        print("El numero", n1, " es menor que: ",n2)
elif n1>n2:
        print("El numero", n2," es mayor que: ",n1)