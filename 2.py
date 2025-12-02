n = int(input("Введите количество чисел Фибоначчи: "))
if n <= 0:
    fib = []
elif n == 1:
    fib = [1]
elif n == 2:
    fib = [1, 1]
else:
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

print("Первые", n, "чисел Фибоначчи:")
print(fib[:n])