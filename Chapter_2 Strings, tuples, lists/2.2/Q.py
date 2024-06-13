al_friend = dict()
new = set()
al_friend2 = dict()
s1 = ''
while (s := input()) != '':
    for elem in s.split(' '):
        if elem not in al_friend:
            al_friend[elem] = s.replace(elem, '').split()
        else:
            al_friend[elem] += s.replace(elem, '').split()

for key, val in al_friend.items():
    for elem in val:
        for elem1 in al_friend[elem]:
            if elem1 != key and elem1 not in al_friend[key]:
                new.add(elem1)
    al_friend2[key] = sorted(new)
    new = set()


for key, val in sorted(al_friend2.items()):
    print(key + ':', end=' ')
    print(*val, sep=', ', end='\n')
