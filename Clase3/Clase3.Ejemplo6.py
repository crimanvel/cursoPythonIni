# Dado tres número enteros distintos, encuentre el mayor y el menor de ellos

n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
n3 = int(input("Ingrese el tercer número entero: "))

if n1 < n2 < n3:
    print("El número mayor es el tercer número")
    print("El número menor es el primero número")
elif n1 < n3 < n2:
    print("El número mayor es el segundo número")
    print("El número menor es el primero número")
elif n2 < n1 < n3:
    print("El número mayor es el tercero número")
    print("El número menor es el segundo número")
elif n2 < n3 < n1:
    print("El número mayor es el primero número")
    print("El número menor es el segundo número")
elif n3 < n1 < n2:
    print("El número mayor es el segundo número")
    print("El número menor es el tercer número")
elif n3 < n2 < n1:
    print("El número mayor es el primero número")
    print("El número menor es el tercer número")
else:
    print("Algunos de los números son iguales")
