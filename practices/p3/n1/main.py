a = int(input())
b = int(input())
c = int(input())

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