def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Вызвано исключение TypeError')
    if not (a > 0 and a % 2 == 0) or not (b > 0 and b % 2 == 0):
        raise ValueError('Вызвано исключение ValueError')
    return a + b


