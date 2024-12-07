'''
Даны положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Не используя операции умножения и деления, найти количество отрезков B, размещенных на отрезке A.
'''

a = float(input())
b = float(input())

count = 0
current_length = 0

while current_length + b <= a:
    count += 1
    current_length += b

print(int(count))