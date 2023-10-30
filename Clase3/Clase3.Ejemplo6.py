n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3 or n1 == n2 == n3:
    mayor = n1
    print("El número mayor es:", mayor)
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    print("El número mayor es:", mayor)
else:
    mayor = n3
    print("El número mayor es:", mayor)

if n1 <= n2 and n1 <= n3 or n1 == n2 == n3:
    menor = n1
    print("El número menor es:", menor)
elif n2 <= n1 and n2 <= n3:
    menor = n2
    print("El número menor es:", menor)
else:
    menor = n3
    print("El número menor es:", menor)
