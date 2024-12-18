"""
Описать функцию `power1(A, B)` вещественного типа,
находящую величину A<sup>B</sup> по формуле A<sup>B</sup> = exp(B * ln(A)) (параметры A и B — вещественные).
В случае нулевого или отрицательного параметра A функция возвращает 0.
С помощью этой функции найти степени A<sup>P</sup>, B<sup>P</sup>, C<sup>P</sup>, если даны числа P, A, B, C.
"""


import math

def power1(a, b):
    """
    Вычисляет A^B используя формулу exp(B * ln(A)).
    Возвращает 0, если A <= 0.
    """
    if a > 0:
        return math.exp(b * math.log(a))
    else:
        return 0

p = float(input())
a = float(input())
b = float(input())
c = float(input())

ap = power1(a, p)
bp = power1(b, p)
cp = power1(c, p)

print(round(ap, 2))
print(round(bp, 2))
print(round(cp, 2))