class Trip_JT:
    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date

    def get_info(self):
        return f"{self.date}   {self.start} -> {self.end}"
