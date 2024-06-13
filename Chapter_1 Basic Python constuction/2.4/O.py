a, b, elem = int(input()), int(input()), 1
c = len(str(a * b))
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j % 2 == 0:
            elem = a * j - (i - 1)
        else:
            elem = a * (j - 1) + i
        print(f'{elem:>{c}}', end=' ')
    print('\r')
