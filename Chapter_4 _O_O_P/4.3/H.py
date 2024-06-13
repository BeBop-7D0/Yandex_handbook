class BadCharacterError(Exception):
    # вызывается, если значение состоит не только из латинских букв, цифр и символа нижнего подчёркивания
    pass


class StartsWithDigitError(Exception):
    # вызывается, если значение начинается с цифры
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    a = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
    if not (all([elem in a for elem in name.lower()])):
        raise BadCharacterError('BadCharacterError')
    if name[0].isdigit():
        raise StartsWithDigitError('StartsWithDigitError')
    return name