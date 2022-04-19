def fibonacci(n_th_number: int) -> int:
    if n_th_number == 0:
        return 0

    a = 0
    b = 1

    for i in range(n_th_number):
        b, a = b + a, b

    return a


print(fibonacci(10))  # -> 55
