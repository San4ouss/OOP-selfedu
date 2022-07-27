class PolyLine:
    def __init__(self, *args):
        self.__coords = list(args)

    def add_coord(self, x, y):
        self.__coords.append((x, y))

    def remove_coord(self, indx):
        self.__coords.pop(indx)

    def get_coords(self):
        return tuple(self.__coords)


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(5, 12)
poly.remove_coord(0)
print(poly.get_coords())
