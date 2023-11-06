# Leer números enteros de teclado, hasta que el usuario ingrese el 0.
# Finalmente mostrar la sumatoria de todos los números positivos y negativos ingresados.
print("Ingrese enteros, para finalizar presione cero")
n = int(input("Ingrese un número entero: "))
sumaPositivos = 0
sumaNegativos = 0
while n != 0 :
    if 0 < n:
        sumaPositivos = sumaPositivos + n
    else :
        sumaNegativos = sumaNegativos + n
    n = int (input("Ingrese un número entero: "))
print("La suma de positivo es :", sumaPositivos , "La suma de negativos es: ", sumaNegativos )
print("Fin")