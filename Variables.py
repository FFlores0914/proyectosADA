num1=int(input("Ingrese un numero entero. "))
num2=float(input("Ingrese un numero Real. "))
def suma (a, b):
    return a+b

print ("Resultado.", suma(num1, num2))

#los enteros no tienen un límite fijo en términos de su valor máximo o mínimo. Python 3 utiliza enteros de precisión arbitraria, lo que significa que puedes trabajar con enteros extremadamente grandes o pequeños sin preocuparte por desbordamientos.
#los números de punto flotante son de doble precisión (64 bits según el estándar IEEE 754). Esto significa que la mayor precisión está en el rango de ±1.7 x 10^308, aproximadamente, y la menor magnitud representable es del orden de 10^-308.