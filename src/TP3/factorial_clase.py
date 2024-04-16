class SingletonMetaFactorial(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonFactorial(metaclass=SingletonMetaFactorial):
    def factorial(self):
        x = int(input("Ingrese un numero entero: "))
        result = 1
        for i in range(1, x + 1):
            result *= i
        print("El factorial de", x, "es:", result)

factorial = SingletonFactorial()
factorial.factorial()