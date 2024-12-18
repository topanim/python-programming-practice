"""
Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
"""


def find_duplicates(a):
    """Находит индексы двух одинаковых элементов в списке."""
    seen = {}
    for i, x in enumerate(a):
        if x in seen:
            return [seen[x], i]
        seen[x] = i
    return []


def print_sorted_indices(indices):
    """Выводит индексы в отсортированном порядке."""
    indices.sort()
    print(*indices)


try:
    a = [int(input("Введите следующее число: ")) for i in range(int(input("Введи N: ")))]
    indices = find_duplicates(a)
    if indices:
        print_sorted_indices(indices)
    else:
        print("Одинаковые элементы не найдены")

except ValueError:
    print("Ошибка ввода")
