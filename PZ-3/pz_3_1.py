"""
Даны три целых числа: A, B, C.
Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».
"""

try:
    a = int(input())
    b = int(input())
    c = int(input())
except ValueError:
    print("Некорректные даные, исправь!")
    raise

pos_count = 0

if a > 0:
    pos_count += 1
if b > 0:
    pos_count += 1
if c > 0:
    pos_count += 1

if pos_count == 2:
    print("True")
else:
    print("False")
