"""
Дан список A размера N. Элементы списка вводятся в формате "1, 2, 3, 4".
Вывести элементы списка в следующем порядке: A[1], A[2], A[N], A[N-1], A[3], A[4], A[N-2], A[N-3], … .
"""


def print_list_custom_order(a):
    """Выводит элементы списка в заданном порядке."""
    left = 0
    right = len(a) - 1

    while left < right:
        print(a[left], end=" ")
        left += 1
        if left < right:
            print(a[right], end=" ")
            right -= 1
    if left == right:
        print(a[left], end=" ")
    print()


try:
    a = [int(input("Введите следующее число: ")) for i in range(int(input("Введи N: ")))]

    if a:  # Проверяем, что список успешно создан
        print_list_custom_order(a)

except Exception as e:
    print(f"Произошла ошибка: {e}")
