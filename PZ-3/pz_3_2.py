"""
Даны три целых числа, одно из которых отлично от двух других, равных между собой.
Определить порядковый номер числа, отличного от остальных.
"""

try:
    a = int(input())
    b = int(input())
    c = int(input())
except ValueError:
    print("Некорректные даные, исправь!")
    raise

if a == b:
    print(3)
elif a == c:
    print(2)
else:
    print(1)