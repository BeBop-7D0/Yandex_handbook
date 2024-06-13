p = ['']
an = set()
while (s := (input())) != '':
    for elem in s.split():
        p.append(elem)
    p.append('')
    for i in range(1, len(p) - 1):
        if p[i - 1] == 'зайка' or p[i + 1] == 'зайка':
            an.add(p[i])
    p = ['']
print(*[elem for elem in an], sep='\n')
