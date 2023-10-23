# Construya un menú que pidal al usuario datos y los guarde y presente en pantalla

print("******************************")
print("**     Menú de Gestión     ***")
print("*                            *")
print("*  Elija el número de opción *")
print("*                            *")
print("*    1- Ingrese su nombre:   *")
print("*    2- Ingrese su apellido: *")
print("*    3- Ingrese su dni:      *")
print("*    4- Presentar datos      *")
print("*    5-Salir                 *")
print("*                            *")
print("******************************")

seleccion = int(input(": "))

if seleccion == 1:
    nombre = input("Ingrese su nombre: ")
elif seleccion == 2:
    apellido = input("Ingrese su apellido: ")
elif seleccion == 3:
    dni = input("Ingrese su Dni: ")
elif seleccion == 4:
    print("Su nombre es: ",nombre )
    print("Su apellido es: ",apellido)
    print("Su DNI es: ",dni)
elif seleccion == 5:
    pass
else:
    pass