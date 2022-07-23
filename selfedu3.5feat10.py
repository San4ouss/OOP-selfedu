class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_thing(self):
        return self.box

    def __eq__(self, other):
        if len(self.box) != len(other.box):
            return False
        first_box = {i.name: i.mass for i in self.box}
        second_box = {i.name: i.mass for i in other.box}
        for i in first_box.items():
            if i[0] not in second_box.keys() or i[1] not in second_box.values():
                return False
        else:
            return True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Локальное свойство name должно иметь тип str")
        if key == "mass" and not isinstance(value, (int, float)):
            raise AttributeError("Локальное свойство mass должно иметь тип int или float")

        object.__setattr__(self, key, value)

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True

print(res)
