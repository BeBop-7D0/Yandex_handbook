s = [elem for elem in input().split()]
s1 = []
result = 0
for i in range(len(s)):
    if s[i] not in ('*', '+', '-'):
        s1.append(int(s[i]))
    else:
        if s[i] == '-':
            result = s1[- 2] - s1[- 1]
            s1.pop(- 2), s1.pop(- 1)
            s1.append(result)
        if s[i] == '*':
            result = s1[- 2] * s1[- 1]
            s1.pop(- 2), s1.pop(- 1)
            s1.append(result)
        if s[i] == '+':
            result = s1[- 2] + s1[- 1]
            s1.pop(- 2), s1.pop(- 1)
            s1.append(result)
print(result)
