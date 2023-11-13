# Posición en que está un elemento
lista = [21,36,122,21,69,4,36,14]
print(lista.index(21))

# Comprobar si un elemento está en la lista
print(36 in lista) # Verdadero o False
print(38 in lista) 

#  Sacar un elemento existente en la lista 
lista.remove(36) # Saco el primer 36
print(lista)

lista.remove(36) # Saco el segundo 36
print(lista)

# Sacar el último elemento de la lista
lista.pop()
print(lista)