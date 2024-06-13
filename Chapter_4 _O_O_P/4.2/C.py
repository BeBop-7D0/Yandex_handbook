class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        if x is None and y is None:
            super().__init__(x=0, y=0)
        elif type(x) is tuple:
            super().__init__(x=self.x[0], y=self.x[1])
        else:
            super().__init__(x=self.x, y=self.y)

    def __str__(self):
        return f"{(self.x, self.y)}"

    def __repr__(self):
        return f"PatchedPoint{self}"

    def __add__(self, other):
        return PatchedPoint(round(self.x + other[0], 2), round(self.y + other[1], 2))

    def __iadd__(self, other):
        self.x += round(other[0], 2)
        self.y += round(other[1], 2)
        return self