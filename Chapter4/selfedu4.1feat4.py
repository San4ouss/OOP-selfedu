class Animal:
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old

    def get_info(self):
        if isinstance(self, Cat):
            return f"{self.name}: {self.old}, {self.color}, {self.weight}"
        elif isinstance(self, Dog):
            return f"{self.name}: {self.old}, {self.breed}, {self.size}"
        else:
            return None

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Атрибут name должен иметь тип str")
        if key == "old" and type(value) != int:
            raise AttributeError("Атрибут old должен иметь тип int")
        object.__setattr__(self, key, value)


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: (int, float)):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def __setattr__(self, key, value):
        if key == "color" and not isinstance(value, str):
            raise AttributeError("Атрибут name должен иметь тип str")
        if key == "weight" and not isinstance(value, (int, float)):
            raise AttributeError("Атрибут weight должен иметь тип int или float")
        if key == "weight" and value < 0:
            raise AttributeError("Атрибут weight должен быть положительным")
        object.__setattr__(self, key, value)


class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def __setattr__(self, key, value):
        if key == "breed" and not isinstance(value, str):
            raise AttributeError("Атрибут breed должен иметь тип str")
        if key == "size" and not isinstance(value, tuple):
            raise AttributeError("Атрибут size должен иметь тип tuple")
        object.__setattr__(self, key, value)


cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())

dog = Dog("пес", 5, "white", (2, 5))
print(dog.get_info())
