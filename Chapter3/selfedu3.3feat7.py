from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.__coords = [0] * args[0]
        else:
            self.__coords = list(args)

    def set_coords(self, *args):
        if len(self.__coords) <= len(args):
            self.__coords = list(args)[:len(self.__coords)]
        else:
            self.__coords[:len(args)] = list(args)
        # n = min(len(args), len(self.__coords))
        # self.__coords[:n] = list(args[:n])

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sqrt(sum(map(lambda x: x ** 2, self.__coords)))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(-5, -3, 12, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords())
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)
