class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, indx):
        self.budget.pop(indx)

    def get_items(self):
        return self.budget


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Атрибут name должен иметь тип str")
        if key == "money" and not isinstance(value, (int, float)):
            raise AttributeError("Атрибут value должен иметь тип int или float")
        object.__setattr__(self, key, value)

    def __add__(self, other):
        sc = other
        if isinstance(other, Item):
            sc = other.money

        return self.money + sc

    def __radd__(self, other):
        return self + other


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)

a = Item("Курс по Python ООП", 2000) + Item("Курс по Django", 5000.01) + Item("Курс по C++", 1500.10) + 500
print(a)
