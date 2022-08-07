class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []

    def add_thing(self, thing):
        if sum([i.weight for i in self.bag]) + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

        self.bag.append(thing)

    def check_indx(self, indx):
        if indx >= len(self.bag):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.check_indx(key)

        lst = self.bag.copy()
        lst[key] = value
        if sum([i.weight for i in lst]) > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        else:
            self.bag[key] = value

    def __delitem__(self, key):
        self.check_indx(key)
        del self.bag[key]


class Thing:
    def __init__(self, name: str, weight: (int, float)):
        self.name = name
        self.weight = weight

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Атрибут name должен иметь тип str")
        if key == "weight" and not isinstance(value, (int, float)):
            raise AttributeError("Атрибут weight должен иметь тип int или float")
        object.__setattr__(self, key, value)


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
