class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def print_date(self):
        print(f"{self.year}年{self.month}月{self.day}日")