
def merge(a, b):
    i, j, c = 0, 0, []
    while len(c) != len(a + b):
        if j == (len(b)) or (i <= (len(a) - 1) and a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return tuple(c)


