import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(rango):
    desde, hasta = map(int, rango.split('-'))
    resultados = []
    if desde == 0:
        desde = 1
    if hasta == 0: 
        hasta = 60
    for num in range(desde, hasta + 1):
        resultados.append(factorial(num))
    return resultados

if len(sys.argv) < 2:
    rango = input("Ingrese el rango en el formato desde-hasta: ")
else:
    rango = sys.argv[1]

resultados = calcular_factoriales(rango)
print("Factoriales en el rango", rango, ":", resultados)