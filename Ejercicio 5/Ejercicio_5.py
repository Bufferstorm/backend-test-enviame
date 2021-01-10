from math import sqrt


def divisorGenerator(n):
    large_divisors = []
    # Iterar sobre los posibles divisores
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def fibonacci_divisor_counter():
    sum = 1
    fib1 = 0
    fib2 = 1
    # Ciclo para revisar cual tiene más de 1k divisores
    while len(list(divisorGenerator(sum))) < 1000:
        sum = fib1+fib2
        print(sum, len(list(divisorGenerator(sum))))
        fib1 = fib2
        fib2 = sum
    return sum


# print(get_divisor_number(8))
print('El número de la sucesión de Fibonacci con más de 1000 divisores es: ', fibonacci_divisor_counter())



