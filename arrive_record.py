from date import Date

class Arrive_Record:
    def __init__(self, date, info):
        self.date = date
        self.info = info

    def print_arrive_record(self):
        print(f"{self.date.year}年{self.date.month}月{self.date.day}日： {self.info}")

