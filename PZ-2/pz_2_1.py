"""
Дано трехзначное число. Найти сумму и произведение его цифр.
"""

try:
    n = int(input())
except ValueError:
    print("Некорректные даные, исправь!")
    raise

a = n // 100
b = (n % 100) // 10
c = n % 10

sum_digits = a + b + c
prod_digits = a * b * c

print(sum_digits)
print(prod_digits)