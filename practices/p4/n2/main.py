a = float(input())
b = float(input())

count = 0
current_length = 0

while current_length + b <= a:
    count += 1
    current_length += b

print(int(count))