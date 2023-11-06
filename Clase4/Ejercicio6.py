# Leer números enteros de teclado, hasta que el usuario ingrese el 0.
# Finalmente mostrar la sumatoria de todos los números positivos ingresados.
print("Ingrese enteros, para finalizar presione cero")
n = int(input("Ingrese un número entero: "))
suma = 0
while n != 0 :
    if 0 < n:
        suma = suma + n
    n = int (input("Ingrese un número entero: "))
print("La suma es ", suma)
print("Fin")