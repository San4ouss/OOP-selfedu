class Integer:
    def __init__(self, start_value=0):
        self.__start_value = start_value

    @property
    def value(self):
        return self.__start_value

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__start_value = value

    def __repr__(self):
        return str(self.__start_value)


class Float:
    def __init__(self, start_value=0.0):
        self.__start_value = start_value

    @property
    def value(self):
        return self.__start_value

    @value.setter
    def value(self, value):
        if type(value) != float:
            raise ValueError('должно быть вещественное число')
        self.__start_value = value

    def __repr__(self):
        return str(self.__start_value)


class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for _ in range(self.__max_length)]

    def check_indx(self, indx):
        if type(indx) != int or indx < 0 or indx >= len(self.__array):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.__array[item].value

    def __setitem__(self, key, value):
        self.check_indx(key)
        self.__array[key].value = value

    def __repr__(self):
        return " ".join(map(str, self.__array))


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1  # должно генерироваться исключение IndexError
