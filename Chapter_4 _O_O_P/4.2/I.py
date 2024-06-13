class Fraction:
    def __init__(self, val_1, val_2=None):
        if val_2 is None:
            if str(val_1).find('/') != -1:
                self.a = int(str(val_1).split('/')[0])
                self.b = int(str(val_1).split('/')[1])
            else:
                self.a, self.b = int(val_1), 1
        else:
            self.a = val_1
            self.b = val_2

        self.__reduction()

    @staticmethod
    def __nod(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def reverse(self):
        old_num = self.numerator()
        old_den = self.denominator()
        self.a = self.__sign() * old_den
        self.b = old_num
        return self

    def __reduction(self):
        __nod = self.__nod(self.a, self.b)
        self.a //= __nod
        self.b //= __nod
        if self.b < 0:
            self.a = -self.a
            self.b = abs(self.b)

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __sign(self):
        return -1 if self.a < 0 else 1

    def __repr__(self):
        return f"Fraction('{self.a}/{self.b}')"

    def numerator(self, val=None):
        if val is None:
            return abs(self.a)
        else:
            self.a = self.__sign() * val
            self.__reduction()

    def denominator(self, val=None):
        if val is None:
            return abs(self.b)
        else:
            self.b = val
            self.__reduction()

    def __neg__(self):
        return Fraction(-self.a, self.b)

    def __znam(self, other):
        new_a1 = self.a * other.b
        new_a2 = other.a * self.b
        return self.b * other.b, new_a1, new_a2

    def __add__(self, other):
        val = other
        if not (isinstance(other, Fraction)):
            val = Fraction(other)
        new_num = Fraction.__znam(self, val)[1] + Fraction.__znam(self, val)[2]
        new_den = Fraction.__znam(self, val)[0]
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        val = other
        if not (isinstance(other, Fraction)):
            val = Fraction(other)
        new_num = Fraction.__znam(self, val)[1] - Fraction.__znam(self, val)[2]
        new_den = Fraction.__znam(self, val)[0]
        return Fraction(new_num, new_den)

    def __iadd__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        self.a = (Fraction.__znam(self, other)[1] + Fraction.__znam(self, other)[2])
        self.b = (Fraction.__znam(self, other)[0])
        self.__reduction()
        return self

    def __isub__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(int(other))
        self.a = (Fraction.__znam(self, other)[1] - Fraction.__znam(self, other)[2])
        self.b = (Fraction.__znam(self, other)[0])
        self.__reduction()
        return self

    def __mul__(self, other):
        if not (isinstance(other, Fraction)):
            return Fraction(self.a * other, self.b)
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        if not (isinstance(other, Fraction)):
            return Fraction(self.a // other, self.b)
        return Fraction(self.a * other.b, self.b * other.a)

    def __imul__(self, other):
        if not (isinstance(other, Fraction)):
            self.a *= other
        else:
            self.a *= other.a
            self.b *= other.b
        self.__reduction()
        return self

    def __itruediv__(self, other):
        if not (isinstance(other, Fraction)):
            self.a //= other
        else:
            self.a *= other.b
            self.b *= other.a
        self.__reduction()
        return self

    def __lt__(self, other):
        if not (isinstance(other, Fraction)):
            return self.a / self.b < other / 1
        return self.a / self.b < other.a / other.b

    def __eq__(self, other):
        if not (isinstance(other, Fraction)):
            return self.a / self.b == other / 1
        return self.a / self.b == other.a / other.b

    def __le__(self, other):
        if not (isinstance(other, Fraction)):
            return self.a / self.b <= other / 1
        return self.a / self.b <= other.a / other.b

    def __ge__(self, other):
        val = other
        if not (isinstance(other, Fraction)):
            return self.a / self.b >= val / 1
        return self.a / self.b >= val.a / val.b

