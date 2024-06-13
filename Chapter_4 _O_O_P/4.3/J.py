from hashlib import *


class MinLengthError(Exception):
    # вызывается, если пароль меньше заданной длины;
    pass


class PossibleCharError(Exception):
    # вызывается, если в пароле используется недопустимый символ;
    pass


class NeedCharError(Exception):
    #  вызывается, если в пароле не найдено ни одного обязательного символа.
    pass


def password_validation(password, min_length=8, possible_chars='qwertyuiopasdfghjklzxcvbnm1234567890',
                        at_least_one=str.isdigit):

    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError('MinLengthError')

    if not (all(map(lambda x: x in possible_chars, password.lower()))):
        raise PossibleCharError('PossibleCharError')

    if not any(map(at_least_one, password.lower())):
        raise NeedCharError('NeedCharError')

    return sha256(password.encode()).hexdigest()