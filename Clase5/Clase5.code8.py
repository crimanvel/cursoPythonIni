listaNombre= ["Paulo","Miguel","Alfredo","Leticia","Francisco","Mariana"]
#print(listaNombre)
#listaNombre.sort()
#print(listaNombre)

#listaNombre.sort(reverse=True)
#print(listaNombre)

# Para ordenar por longitud de las es
#listaNombre.sort(key=len)
#print(listaNombre)

listaNombre.sort(key=len,reverse=True)
print(listaNombre)