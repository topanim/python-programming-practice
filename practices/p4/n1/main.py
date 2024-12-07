'''
Дано вещественное число A и целое число N (>0). Используя один цикл, найти значение выражения 1 - A + A2 - A3 + ... +(-1)NAN. Условный оператор не использовать.
'''

a = float(input())
n = int(input())

result = 1
sign = -1

for i in range(1, n + 1):
  result = result + sign * (a ** i)
  sign = sign * -1


print(result)