import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    x_values = []  # Número de iteraciones
    y_values = []  # Número inicial de la secuencia
    for n in range(1, 10001):
        sequence = collatz_sequence(n)
        iterations = len(sequence) - 1  # El número de iteraciones es la longitud de la secuencia menos 1
        x_values.append(iterations)
        y_values.append(n)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'bo', markersize=1)  # 'bo' para puntos azules
    plt.title('Número de Collatz')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Número Inicial de la Secuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()