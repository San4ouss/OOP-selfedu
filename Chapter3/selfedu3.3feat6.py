from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)

    def __abs__(self):
        return sqrt(self.__real ** 2 + self.__img ** 2)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

print(c_abs)
print(cmp.__dict__)
