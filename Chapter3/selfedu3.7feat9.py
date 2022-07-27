class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __check_other(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            return other.coords
        else:
            return other

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            return Vector(*[self.coords[i] + sc for i in range(len(self.coords))])
        return Vector(*[self.coords[i] + sc[i] for i in range(len(self.coords))])

    def __iadd__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            self.coords = [self.coords[i] + sc for i in range(len(self.coords))]
        else:
            self.coords = [self.coords[i] + sc[i] for i in range(len(self.coords))]
        return self

    def __sub__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            return Vector(*[self.coords[i] - sc for i in range(len(self.coords))])
        return Vector(*[self.coords[i] - sc[i] for i in range(len(self.coords))])

    def __isub__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            self.coords = [self.coords[i] - sc for i in range(len(self.coords))]
        else:
            self.coords = [self.coords[i] - sc[i] for i in range(len(self.coords))]
        return self

    def __mul__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            return Vector(*[self.coords[i] * sc for i in range(len(self.coords))])
        return Vector(*[self.coords[i] * sc[i] for i in range(len(self.coords))])

    def __imul__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            self.coords = [self.coords[i] * sc for i in range(len(self.coords))]
        else:
            self.coords = [self.coords[i] * sc[i] for i in range(len(self.coords))]
        return self

    def __eq__(self, other):
        sc = self.__check_other(other)
        if isinstance(sc, (int, float)):
            raise ArithmeticError("Сравнение должно проходить только между объектами класса Vector")
        return bool([i for i in range(len(self.coords)) if self.coords[i] == sc[i]])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
# print((v1 + v2).coords)  # [5, 7, 9]
# print((v1 - v2).coords)  # [-3, -3, -3]
# print((v1 * v2).coords)  # [4, 10, 18]
#
# v1 += 10
# print(v1.coords)  # [11, 12, 13]
# v1 -= 10
# print(v1.coords)  # [1, 2, 3]
# v1 += v2
# print(v1.coords)  # [5, 7, 9]
# v2 -= v1
# print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
