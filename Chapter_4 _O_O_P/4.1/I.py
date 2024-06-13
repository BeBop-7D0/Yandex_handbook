class Queue:
    def __init__(self):
        self.mass = []

    def push(self, item):
        self.mass.append(item)

    def pop(self):
        return self.mass.pop(0)

    def is_empty(self):
        return len(self.mass) == 0

