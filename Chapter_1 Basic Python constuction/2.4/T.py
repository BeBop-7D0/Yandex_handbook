
N_max, sum1, i_max, N = 0, 0, 0, int(input())
for i in range(2, 11):
    sum1, ost, s = 0, N // i, str(N % i)
    while ost > i:
        s += str(ost % i)
        ost = ost // i
    s += str(ost)
    for elem in s:
        sum1 += int(elem)
    if sum1 > N_max:
        N_max, i_max = sum1, i
print(i_max)
