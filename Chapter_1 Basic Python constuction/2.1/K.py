abcd = int(input())
a = str(abcd // 1000)
b = str(abcd // 100 % 10)
c = str(abcd // 10 % 10)
d = str(abcd % 10)
print(b + a + d + c)
