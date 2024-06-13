n = input().split()
f = ''
for elem in n:
    f += elem
if len(f.lower()) % 2 != 0:
    if f.lower()[: len(f.lower()) // 2] == f.lower()[len(f.lower()):len(f.lower()) // 2: - 1]:
        print('YES')
    else:
        print('NO')
else:
    if f.lower()[: len(f.lower()) // 2] == f.lower()[len(f.lower()):len(f.lower()) // 2 - 1: - 1]:
        print('YES')
    else:
        print('NO')
