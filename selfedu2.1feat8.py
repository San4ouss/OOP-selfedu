class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__sp = (x1, y1)
        self.__ep = (x2, y2)

    def set_coords(self, sp, ep):
        pass
