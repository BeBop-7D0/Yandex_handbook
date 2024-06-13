f = {'digits': 0,
     'units': 0,
     'zeros': 0}
r = {}
p = []
i = 0
for N in input().split():
    ost = int(N) // 2
    s = str(int(N) % 2)
    while ost >= 2:
        s += str(ost % 2)
        ost = ost // 2
    s += str(ost)
    if N == '1' or N == '0':
        s = s[:len(s) - 1]
    f['digits'] = len(s)
    f['units'] = s.count('1')
    f['zeros'] = s.count('0')
    r = f.copy()
    p.append(r)
    r = 0
print(p)

