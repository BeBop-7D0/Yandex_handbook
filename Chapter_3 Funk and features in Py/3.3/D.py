def answer(func):
    def decor(*values, **kwargs):
        return f"Результат функции: {func(*values, **kwargs)}"
    return decor
