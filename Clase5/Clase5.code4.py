miLista = [
    3.21,
    263,
    369,
    147,
    69,
    14,
    369,
    177,
    16,
    36,
    1474,
    "Hola",
    "hoy es 13 de noviembre",
    3.12,
    -8,
    "h",
]

print(miLista)
# Agregar un elemento al final de la lista
# Agregamos "Final de la lista"

miLista.append("Final de la lista")
print(miLista)

# Quiero agregar un mensaje que diga "Inicio" al principio de la lista
miLista.insert(0,"Inicio")
print(miLista)

# Quiero agregar los elementos "Hola",21,11,-3.2 al final de la lista
miLista.extend(["Hola",21,11,-3.2])
print(miLista)