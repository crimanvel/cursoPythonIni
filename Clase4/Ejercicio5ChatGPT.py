# Leer números enteros de teclado hasta que el usuario ingrese el cero
# Finalmente, mostrar la sumatoria de todos los números ingresados
suma = 0
while True:
    numero =int(input("Ingrese un número entero (0 para terminar):"))
    if numero == 0:
        break
    suma += numero
print("La suma de los números ingresados es: ", suma)