class Cell:
    def __init__(self, st):
        self.st = st

    def status(self):
        return self.st


class Checkers:
    def __init__(self):
        self.cells = {}
        i = 0
        j = 0
        for coll in '87654321':
            for roww in 'ABCDEFGH':
                if ((i + j) % 2 != 0) and (i < 3):
                    self.cells[roww + coll] = Cell('B')
                elif ((i + j) % 2 != 0) and (i > 4):
                    self.cells[roww + coll] = Cell('W')
                else:
                    self.cells[roww + coll] = Cell('X')
                j += 1
            i += 1

    def get_cell(self, p):
        return self.cells[p]

    def move(self, f, t):
        self.cells[f], self.cells[t] = Cell('X'), self.cells[f]