n_str = input("Введите количество чисел Фибоначчи: ")
if n_str.isdigit() and int(n_str) > 0:
    n = int(n_str)
    if n == 1:
        fib = [1]
    elif n == 2:
        fib = [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])

    print("Первые", n, "чисел Фибоначчи:")
    print(fib)
else:
    print("Ошибка: нужно ввести целое положительное число.")