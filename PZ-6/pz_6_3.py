"""
Дан список A размера N и целое число K (1 < K < 4, K < N).
Осуществить циклический сдвиг элементов списка вправо на K позиций
(при этом A[1] перейдет в A[K+1], A[2] — в A[K+2], ..., A[N] — в A[K]).
Допускается использовать вспомогательный список из 4 элементов.
"""


def cyclic_shift(a, k):
    """Осуществляет циклический сдвиг списка a вправо на k позиций."""
    n = len(a)
    temp = a[n - k:]  # Используем срезы для создания копии последних k элементов
    for i in range(n - 1, k - 1, -1):
        a[i] = a[i - k]
    for i in range(k):
        a[i] = temp[i]


try:
    a = [int(input("Введите следующее число: ")) for i in range(int(input("Введи N: ")))]
    k = int(input("Введите число K (1 < K < 4 и K < N): "))
    if 1 < k < 4 and k < len(a):
        cyclic_shift(a, k)
        print(*a)  # Вывод элементов списка через пробел
    else:
        print("Некорректное значение K")
except ValueError:
    print("Ошибка ввода")
