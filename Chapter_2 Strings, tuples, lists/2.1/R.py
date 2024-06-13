s = [elem for elem in input()]
k = 1
s.append(' ')
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
    else:
        print(s[i], k)
        k = 1
