class Factorial:
    def __init__(self):
        pass
    
    def calcular_factorial(self, num):
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

    def run(self, min_num, max_num):
        resultados = {}
        for num in range(min_num, max_num + 1):
            resultados[num] = self.calcular_factorial(num)
        return resultados

if __name__ == "__main__":
    factorial_calculator = Factorial()
    min_num = int(input("Ingrese el número mínimo del rango: "))
    max_num = int(input("Ingrese el número máximo del rango: "))
    resultados = factorial_calculator.run(min_num, max_num)
    print("Factoriales en el rango", min_num, "-", max_num, ":", resultados)