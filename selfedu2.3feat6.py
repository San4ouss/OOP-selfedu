class FloatValue:
    @staticmethod
    def check_data(data):
        if not isinstance(data, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        return data

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_data(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(0.0)] * M] * N


table = TableSheet(3, 5)
for i in table.cells:
    print(*i)

for i in table.cells:
    for j in range(len(i)):
        pass

print(isinstance(0.0, float))

lst = [[Cell(0.0).value] * 5] * 3
print(lst)
for i in lst:
    print(*i)
