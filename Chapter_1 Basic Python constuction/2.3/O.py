k, num1 = 0, 0
for i in range(int(input())):
    if 'зайка' in input():
        k = 1
    if k == 1:
        num1 += 1
    k = 0
print(num1)
