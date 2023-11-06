# Leer números enteros de teclado hasta que el usuario ingrese el cero
# Finalmente, mostrar la sumatoria de todos los números ingresados
n = int(input("Ingrese un número entero: "))
suma = 0
while 0 != n :
    suma = suma + n
    n = int (input("Ingrese un número entero: "))
print("La suma es ", suma)
print("Fin")