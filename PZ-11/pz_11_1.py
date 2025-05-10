"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Положительные числа:
Количество положительных чисел:
Отрицательные числа:
Количество отрицательных чисел:
"""

# Формирование текстовых файлов с последовательностью чисел
import random

try:
    # Создаем исходный файл с последовательностью чисел
    numbers = [random.randint(-100, 100) for _ in range(20)]  # Пример: 20 случайных чисел
    with open('numbers.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, numbers)))

    # Обработка чисел
    positive = [n for n in numbers if n > 0]
    negative = [n for n in numbers if n < 0]

    # Создаем результирующий файл
    with open('numbers_result.txt', 'w', encoding='utf-8') as f:
        f.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
        f.write(f"Количество элементов: {len(numbers)}\n")
        f.write(f"Положительные числа: {' '.join(map(str, positive))}\n")
        f.write(f"Количество положительных чисел: {len(positive)}\n")
        f.write(f"Отрицательные числа: {' '.join(map(str, negative))}\n")
        f.write(f"Количество отрицательных чисел: {len(negative)}\n")

except IOError:
    print("Ошибка при работе с файлами")
except Exception as e:
    print(f"Произошла ошибка: {e}")