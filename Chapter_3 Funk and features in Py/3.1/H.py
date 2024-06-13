
def is_palindrome(x):
    if type(x) is int or type(x) is float:
        x = str(abs(x))
    return x == x[::-1]


