s = [elem for elem in input().split()]
s1 = []
result = 0
n = 1
el1, el2, el3 = 0, 0, 0
for i in range(len(s)):
    if s[i] not in ('*', '+', '-', '/', '!', '~', '#', '@'):
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
        if s[i] == '/':
            result = s1[- 2] // s1[- 1]
            s1.pop(- 2), s1.pop(- 1)
            s1.append(result)
        if s[i] == '~':
            result = - s1[- 1]
            s1.pop(- 1)
            s1.append(result)
        if s[i] == '#':
            result = s1[- 1]
            s1.append(result)
        if s[i] == '!':
            for j in range(1, s1[-1] + 1):
                n *= j
            result = n
            s1.pop(-1)
            s1.append(result)
        if s[i] == '@':
            el1 = s1[-3]
            el2 = s1[-2]
            el3 = s1[-1]
            s1.pop(- 3)
            s1.pop(- 2)
            s1.pop(- 1)
            s1.append(el2), s1.append(el3), s1.append(el1)
print(result)
