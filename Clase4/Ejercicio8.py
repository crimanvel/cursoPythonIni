# Leer un número entero positivo desde el teclado e imprimir la suma de los dígitos que lo componen
numero = int(input("Ingrese un entero positivo: "))
sumaCifras = 0
while 0 < numero:
    cifra = numero % 10
    numero = numero // 10
    sumaCifras = sumaCifras + cifra
print("La suma de cifras es: ", sumaCifras)
