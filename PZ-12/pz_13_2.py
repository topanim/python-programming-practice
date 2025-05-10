"""
Составить генератор (yield), который переведет символы строки из нижнего
регистра в верхний.
"""

def to_uppercase(s):
    """Генератор для перевода символов строки в верхний регистр"""
    for char in s:
        yield char.upper()

try:
    input_string = "Hello, World!"  # Пример строки
    print(f"Исходная строка: {input_string}")
    result = ''.join(to_uppercase(input_string))
    print(f"Результирующая строка: {result}")
except TypeError:
    print("Ошибка: Входные данные должны быть строкой")