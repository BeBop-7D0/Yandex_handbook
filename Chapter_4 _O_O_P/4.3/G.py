class CyrillicError(Exception):
    # вызывается, если значение не состоит только из кириллических букв
    pass


class CapitalError(Exception):
    # вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква не в начале значения
    pass


def name_validation(f_n):
    cir = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    if not isinstance(f_n, str):
        raise TypeError
    if not (all([elem.lower() in cir for elem in f_n])):
        raise CyrillicError('CyrillicError')
    if not (str(f_n)[0].isupper()) or not (all([elem.islower() for elem in str(f_n)[1:]])):
        raise CapitalError('CapitalError')
    return f_n  