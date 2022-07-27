class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(tm):
        if isinstance(tm, int) and 0 <= tm < 100000:
            return True
        else:
            return False


clock = Clock(4530)

clock.set_time(500)
clock.set_time("1000")
print(clock.get_time())
