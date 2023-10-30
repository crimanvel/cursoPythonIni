# Realice un programa que pida un número de del 
# día del 1 al 7 y presente el nombre del día que corresponde según la tabla: 
# lunes=1, martes=2, miercoles=3, jueves=4, viernes=5, sabado=6, domingo=7

numeroDia = int(input("Ingrese un número entero del 1 al 7:"))

if numeroDia == 1 :
    print("Es lunes")
elif numeroDia == 2 :
    print("Es martes")
elif numeroDia == 3:
    print("Es miercoles")
elif numeroDia == 4 :
    print("Es Jueves")
elif numeroDia == 5 :
    print("Es viernes")
elif numeroDia == 6 :
    print("Es sábado")
elif numeroDia == 7 :
    print("Es domingo")
else: 
    print("Número invalido")