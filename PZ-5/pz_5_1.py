"""
Найти сумму чисел ряда 1, 2, 3, 4,... от числа n до числа m.
Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.
"""

def calculate_sum(n, m):
    """
    Вычисляет сумму чисел от n до m включительно.
    """
    sum = 0
    for i in range(n, m + 1):
        sum += i
    return sum

n = int(input())
m = int(input())


if n <= m:
    result = calculate_sum(n, m)
    print(result)
else:
    print("n должно быть меньше или равно m")