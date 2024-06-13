from itertools import combinations

deti = set()
for i in range(int(input())):
    deti.add(input())
for val in combinations(deti, 2):
    print(val[0], '-', val[1])
