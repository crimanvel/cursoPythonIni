# Pida dos numeros enteros y calcule la suma (+), resta (-), multiplicación (*), division (/), mod (%) y div (//)
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

sum = numero1 + numero2
res = numero1 - numero2
mult = numero1 * numero2
divi = numero1 / numero2
mod = numero1 % numero2
div = numero1 // numero2

print(
    "La suma es: ",
    sum,
    "La resta es: ",
    res,
    "La multiplicación es: ",
    mult,
    "La división es: ",
    divi,
    "El modulo es:",
    mod,
    "El div es: ",
    div,
)
