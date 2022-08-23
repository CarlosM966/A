#Aplicar el IVA al precio de un producto.
print("Ingresa el valor del producto: ")
precioCompra = float(input())
IVA = precioCompra * 0.15
total = precioCompra + IVA
print("El total es:", total)