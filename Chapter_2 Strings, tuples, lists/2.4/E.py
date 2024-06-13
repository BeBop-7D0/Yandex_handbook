mag = set()
for i in range(3):
    for elem in input().split(', '):
        mag.add(elem)
for index, val in enumerate(sorted(mag), 1):
    print(str(index) + '.', val)