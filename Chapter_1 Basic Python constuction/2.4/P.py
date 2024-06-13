a, b = int(input()), int(input())
c = 0
for i in range(1, a + 1):

    for j in range(1, a + 1):
        print(f'{i * j:^{b}}', end='')
        if j != a:
            print('|', end='')
    print('\r')
    c = b * a + a - 1
    if i != a:
        print(f'{"":->{c}}')
