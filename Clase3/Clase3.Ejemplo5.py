print("******************************")
print("**     Menú                ***")
print("*    1- Sumar:               *")
print("*    2- Restar:              *")
print("*    3- Multiplicar:         *")
print("*    4- Dividir              *")
print("*    5- Mod                  *")
print("*    6- Div                  *")
print("******************************")

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
seleccion = int(input("Indique que operación desea realizar: "))

if 1 <= seleccion <= 6:
    if seleccion == 1:
        resultado = n1 + n2
    elif seleccion == 2:
        resultado = n1 - n2
    elif seleccion == 3:
        resultado = n1 * n2
    elif seleccion == 4:
        resultado = n1 / n2
    elif seleccion == 5:
        resultado = n1 % n2
    elif seleccion == 6:
        resultado = n1 // n2
    print("El resultado de la operacion es: ", resultado)
else:
    print("Opción no valida!")
