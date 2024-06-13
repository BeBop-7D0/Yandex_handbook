
def is_prime(x):
    anw = True
    for i in range(2, int((x ** 0.5) + 1)):
        if (x % i) == 0:
            anw = False
            break
    return anw
