from random import randint


def gen_points():
    return randint(0, 2000), randint(0, 2000)


def get_days(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib1 = 0
    fib2 = 1
    for i in range(n - 1):
        sum = fib1 + fib2
        # print("Valor del i: ", i, "Valor de la suma: ", sum)
        fib1 = fib2
        fib2 = sum
    return sum


def get_delivery_days(start, end):
    print("Dist Inicio: ", start)
    print("Dist Fin: ", end)
    dist = abs(start - end)
    print("Distancia entre ambos puntos: ", dist)
    n = int(dist / 100)
    return get_days(n)


print("Cantidad de días: ", get_delivery_days(gen_points()[0], gen_points()[1]))