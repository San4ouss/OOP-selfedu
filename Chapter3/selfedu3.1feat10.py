import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.dict_slots = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if (isinstance(filter, Mechanical) and slot_num == 1) or (isinstance(filter, Aragon) and slot_num == 2) or \
                (isinstance(filter, Calcium) and slot_num == 3):
            if self.dict_slots[slot_num] is None:
                self.dict_slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.dict_slots[slot_num] = None

    def get_filters(self):
        return tuple(self.dict_slots.values())

    def water_on(self):
        end = time.time()
        for i in self.dict_slots.values():
            if i is None:
                return False
            if 0 > (end - i.date) or (end - i.date) > self.MAX_DATE_FILTER:
                return False

        else:
            return True


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            return object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            return object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            return object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w2 = my_water.water_on()  # True
print(w2)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
