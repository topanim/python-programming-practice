a = float(input())
n = int(input())

result = 1
sign = -1

for i in range(1, n + 1):
  result = result + sign * (a ** i)
  sign = sign * -1


print(result)