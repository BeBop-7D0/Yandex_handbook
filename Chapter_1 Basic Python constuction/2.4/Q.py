k = 0
for i in range(int(input())):
    s = input()
    if len(s) % 2 == 0:
        if (s[0: len(s) // 2]) == (s[len(s): len(s) // 2 - 1: -1]):
            k += 1
    else:
        if (s[0: (len(s) // 2)]) == (s[len(s) + 1: (len(s) // 2): - 1]):
            k += 1
print(k)
