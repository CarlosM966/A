#Mostrar el total a pagar por la compra de n cantidad de productos a un precio
#desconocido.
print("Cantidad de productos: ")
prods = int(input())
i = 0
sub = 0
while i < prods:
    print("Producto",i+1,"valor")
    val = int(input())
    print("Cantidad")
    cant = int(input())
    subPro = val * cant
    i+=1
    total = subPro 

    print("Se vendieron: ",prods,"Productos")
    print("Subtotal: ",sub)
    print("Total: ",total)