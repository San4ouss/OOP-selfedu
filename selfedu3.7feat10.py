class Vector:
    def __init__(self, *args):
        self.coords = list(args[0]) if len(args) == 1 else list(args)

    def __add__(self, other):
        if len(self) != len(other) and isinstance(other, Vector):
            raise ArithmeticError('размерности векторов не совпадают')
        if isinstance(other, (int, float)):
            return Vector([self.coords[i] + other for i in range(len(self.coords))])
        return Vector([self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __len__(self):
        return len(self.coords)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [self.coords[i] + other for i in range(len(self.coords))]
        if len(self) != len(other) and isinstance(other, Vector):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            self.coords = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]

    # def __sub__(self, other):
    #     if len(self) != len(other):
    #         raise ArithmeticError('размерности векторов не совпадают')
    #     if isinstance(other, (int, float)):
    #         return Vector([self.coords[i] - other for i in range(len(self.coords))])
    #     return Vector([self.coords[i] - other.coords[i] for i in range(len(self.coords))])
    #
    # def __isub__(self, other):
    #     if len(self) != len(other):
    #         raise ArithmeticError('размерности векторов не совпадают')
    #     if isinstance(other, (int, float)):
    #         self.coords = [self.coords[i] - other for i in range(len(self.coords))]
    #     else:
    #         self.coords = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
    #
    # def __mul__(self, other):
    #     if len(self) != len(other):
    #         raise ArithmeticError('размерности векторов не совпадают')
    #     if isinstance(other, (int, float)):
    #         return Vector([self.coords[i] * other for i in range(len(self.coords))])
    #     return Vector([self.coords[i] * other.coords[i] for i in range(len(self.coords))])
    #
    # def __imul__(self, other):
    #     if len(self) != len(other):
    #         raise ArithmeticError('размерности векторов не совпадают')
    #     if isinstance(other, (int, float)):
    #         self.coords = [self.coords[i] * other for i in range(len(self.coords))]
    #     else:
    #         self.coords = [self.coords[i] * other.coords[i] for i in range(len(self.coords))]


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
# print((v1 - v2).coords)  # [-3, -3, -3]
# print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
# v1 -= 10
# print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
# v2 -= v1
# print(v2.coords)  # [-1, -2, -3]

# print(v1 == v2)  # False
# print(v1 != v2)  # True







