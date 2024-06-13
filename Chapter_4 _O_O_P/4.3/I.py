class CyrillicError(Exception):
    # вызывается, если значение не состоит только из кириллических букв
    pass


class CapitalError(Exception):
    # вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква не в начале значения
    pass


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


def name_validation(f_n):
    cir = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    if not isinstance(f_n, str):
        raise TypeError
    if not (all([elem.lower() in cir for elem in f_n])):
        raise CyrillicError('CyrillicError')
    if not (str(f_n)[0].isupper()) or not (all([elem.islower() for elem in str(f_n)[1:]])):
        raise CapitalError('CapitalError')
    return f_n


def user_validation(**kwargs):
    s1 = ('last_name', 'first_name', 'username')
    if set(kwargs.keys()) != set(s1):
        raise KeyError
    elif not all([isinstance(elem, str) for elem in [kwargs['last_name'],
                                                     kwargs['first_name'], kwargs['first_name']]]):
        raise TypeError
    else:
        answer = {"last_name": name_validation(kwargs['last_name']),
                  "first_name": name_validation(kwargs['first_name']),
                  "username": username_validation(kwargs['username'])}
        return answer
