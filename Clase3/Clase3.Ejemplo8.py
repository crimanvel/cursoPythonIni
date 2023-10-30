numeroSemana = int(input("Indique un número entero entre 1 a 7: "))

while numeroSemana <1 or 7 < numeroSemana:
    numeroSemana = int(input("Error! Indique un número entero entre 1 a 7: "))
if numeroSemana == 1:
    print("Lunes")
elif numeroSemana == 2:
    print("Martes")
elif numeroSemana == 3:
    print("Miercoles")
elif numeroSemana == 4:
    print("Jueves")
elif numeroSemana == 5:
    print("Viernes")
elif numeroSemana == 6:
    print("Sábado")
elif numeroSemana == 7:
    print("Domingo")
