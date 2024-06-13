a = 1
b = 1001
print(500)
s = input()
while s != "Угадал!":
    if s == 'Больше':
        a = (b + a) // 2
    elif s == 'Меньше':
        b = (b + a) // 2
    print((b + a) // 2)
    s = input()
