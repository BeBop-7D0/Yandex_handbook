det_igr = dict()
Un = set()
al = []
for i in range(int(input())):
    s = input()
    name = s[:s.find(':')]
    det_igr[name] = set(s[s.find(':') + 2:].split(', '))
for elem in det_igr.values():
    for elem1 in elem:
        al.append(elem1)
for elem in al:
    if al.count(elem) != 1:
        Un.add(elem)
al = set(al)
for elem in Un:
    al.remove(elem)
for elem in sorted(al):
    print(elem)
