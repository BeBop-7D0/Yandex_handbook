class Programmer:
    def __init__(self, name, title, work_time=0):
        num = {"Junior": 0, "Middle": 1, "Senior": 2}
        prof = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.name = name
        self.title = title
        self.work_time = work_time
        self.cash = 0
        self.bid = prof[self.title]
        self.title_num = num[self.title]

    def work(self, time):
        self.work_time += time
        self.cash += time * self.bid

    def rise(self):
        num = {0: "Junior", 1: "Middle", 2: "Senior"}
        prof = {"Junior": 10, "Middle": 15, "Senior": 20}
        if self.title_num != 2:
            self.title_num += 1
            self.title = num[self.title_num]
            self.bid = prof[num[self.title_num]]
        else:
            self.bid += 1

    def info(self):
        return f"{self.name} {self.work_time}ч. {self.cash}тгр."
