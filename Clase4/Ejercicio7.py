#Ingresar números enteros positivos por teclado, hasta que el usuario ingrese el cero.
#Informar cual fue el mayot número.
#Suponer que por lo menos ingreso un número distinto a todos los demás.
print("Ingrese números enteros positivos, para terminar ingrese un cero.")

mayor = int(input("Ingrese un número entero: "))
numero = mayor
while numero != 0:
    if mayor < numero:
        mayor = numero
    numero = int(input("Ingrese un número entero: 50"))
print("El mayor número ingresado es: ", mayor)