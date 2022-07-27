class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        #  должен возвращать именно тип данных str
        n = self.clock1.get_time() - self.clock2.get_time()
        return f"{n // 3600:02}: {n % 3600 // 60:02}: {n % 3600 % 60:02}" if n > 0 else "00: 00: 00"

    def __len__(self):
        #  должен возвращать именно тип данных int
        n = self.clock1.get_time() - self.clock2.get_time()
        return n if n > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(10, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
