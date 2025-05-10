# Извлечение цен из текстового файла и подсчёт их количества
import re

try:
    # Читаем файл
    with open('price.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # Извлекаем цены с помощью регулярного выражения
    prices = re.findall(r'\d+\s*руб\.\s*\d+\s*коп\.', content)

    # Выводим найденные цены
    print("Найденные цены:", prices)
    # Подсчитываем количество цен
    print("Количество цен:", len(prices))

except FileNotFoundError:
    print("Ошибка: Файл не найден")
except IOError:
    print("Ошибка при работе с файлами")
except Exception as e:
    print(f"Произошла ошибка: {e}")