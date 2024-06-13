from itertools import islice

kash = []
k = int(input())
for i in range(k):
    kash.append(input())
n = int(input())
while len(kash) < n:
    kash += kash
for val in islice(kash, 0, n):
    print(val)
