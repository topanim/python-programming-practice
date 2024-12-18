"""
Дан список A размера N. Элементы списка вводятся в формате "1, 2, 3, 4".
Вывести элементы списка в следующем порядке: A[1], A[2], A[N], A[N-1], A[3], A[4], A[N-2], A[N-3], … .
"""

def parse_list(input_string):
    """Преобразует строку с элементами списка в список целых чисел."""
    try:
        return [int(x.strip()) for x in input_string.split(',')]
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа, разделенные запятыми.")
        return None  # Возвращаем None в случае ошибки


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
    input_string = input("Введите элементы списка через запятую: ")
    a = parse_list(input_string)

    if a:  # Проверяем, что список успешно создан
        print_list_custom_order(a)

except Exception as e:
    print(f"Произошла ошибка: {e}")