class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([cell() for _ in range(cols)]) for _ in range(rows)])
        # print(self.cells)
        # self.__rows = rows
        # self.__cols = cols
        # self.__cell = cell
        # if cell is None:
        #     raise ValueError('параметр cell не указан')
        # self.cells = [(self.__cell() for _ in range(self.__cols)) for _ in range(self.__rows)]

    def __getitem__(self, item):
        # print(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        # print(key)
        self.cells[key[0]][key[1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
