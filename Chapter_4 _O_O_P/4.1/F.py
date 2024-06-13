class Rectangle:
    def __init__(self, x1y1, x2y2):
        self.x1 = x1y1[0]
        self.y1 = x1y1[1]
        self.x2 = x2y2[0]
        self.y2 = x2y2[1]
        self.dl = round(abs(self.x1 - self.x2), 2)
        self.sh = round(abs(self.y1 - self.y2), 2)

    def perimeter(self):
        return round((self.dl + self.sh) * 2, 2)

    def area(self):
        return round(self.sh * self.dl, 2)

    def get_pos(self):
        return round(min(self.x1, self.x2), 2), round(max(self.y1, self.y2), 2)

    def get_size(self):
        return self.dl, self.sh

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        return (round(self.x1, 2), round(self.y1, 2)), (round(self.x2, 2), round(self.y2, 2))

    def resize(self, width, height):
        self.x1 = round(min(self.x1, self.x2), 2)
        self.y1 = round(max(self.y1, self.y2), 2)
        self.x2 = self.x1 + width
        self.y2 = self.y1 - height
        self.dl = round(abs(self.x1 - self.x2), 2)
        self.sh = round(abs(self.y1 - self.y2), 2)

    def scale(self, val):
        a1 = self.dl
        a2 = a1 * val
        b1 = self.sh
        b2 = b1 * val
        self.x1 = self.get_pos()[0] - (b2 - b1) * 0.5
        self.y1 = self.get_pos()[1] + (a2 - a1) * 0.5
        self.x2 = self.x1 + a2
        self.y2 = self.y1 - b2
        self.dl = a2
        self.sh = b2

    def turn(self):
        centre = ((self.x2 - self.x1) / 2, (self.y2 - self.y1) / 2)
        self.x1 = centre[0] - (self.sh / 2)
        self.y1 = centre[1] - (self.dl / 2)
        self.x2 = self.x1 + self.sh
        self.y2 = self.y1 + self.dl
        self.dl, self.sh = self.sh, self.dl

