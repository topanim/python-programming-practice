"""
Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
"""

# Обработка текстового файла со стихотворением
import string

try:
    # Читаем и выводим содержимое файла
    with open('text18-16.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("Содержимое файла:")
        print(content)

    # Подсчет букв в верхнем регистре
    uppercase_count = sum(1 for c in content if c.isupper())
    print(f"Количество букв в верхнем регистре: {uppercase_count}")

    # Замена пунктуации на '!' и форматирование в стихотворную форму
    translator = str.maketrans('', '', string.punctuation)  # Удаляем пунктуацию
    lines = content.translate(translator).split('\n')
    new_poem = '\n'.join(line.strip() + '!' for line in lines if line.strip())

    # Создаем новый файл
    with open('poem_result.txt', 'w', encoding='utf-8') as f:
        f.write(new_poem)

except FileNotFoundError:
    print("Ошибка: Файл не найден")
except IOError:
    print("Ошибка при работе с файлами")
except Exception as e:
    print(f"Произошла ошибка: {e}")