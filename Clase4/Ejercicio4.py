#Dado dos números enteros positivos distintos sin importar el orden de carga 
# encuentre los valores comprendidos entre ellos
n1= int(input("Ingrese el primer número: "))
n2= int(input("Ingrese el segundo número : "))

if n2 < n1 :
    auxiliar = n1
    n1 = n2
    n2 = auxiliar
n1= n1 +1
while n1 < n2 :
        print(n1)
        n1 = n1 +1    
print("fin")