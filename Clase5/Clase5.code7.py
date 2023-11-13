listaA=[12,36,69,14,13,356]*5
print(listaA)
print(listaA.count(14)) # determinar cuantas veces aparece un elemento en la lista

# quiero ordenar de menor a mayor la lista y presentarla

listaA.sort()
print(listaA)

# quiero ordenar de mayor a menor la lista y presentarla

listaA.sort(reverse=True)
print(listaA)

listaNombre= ["Paulo","Miguel","Alfredo","Leticia","Francisco","Mariana"]
print(listaNombre)
listaNombre.sort()
print(listaNombre)
listaNombre.sort(reverse=True)
print(listaNombre)

# Para ordenar por longitud de las es
listaNombre.sort(key=len)
print(listaNombre)

listaNombre.sort(key=len,reverse=True)
print(listaNombre)