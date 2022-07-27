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

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(float(row * M + col + 1)) for col in range(M)] for row in range(N)]


table = TableSheet(5, 3)

for i in table.cells:
    for j in i:
        print(j.value, end=" ")
