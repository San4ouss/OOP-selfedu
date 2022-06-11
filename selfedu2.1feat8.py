class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__sp = args[0].get_coords()
            self.__ep = args[1].get_coords()
        else:
            self.__sp = args[0]
            self.__ep = args[1]

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}")


rect = Rectangle((0, 0), (20, 34))

# rect.set_coords(Point(0, 0), Point(1, 1))
print(isinstance(rect, Rectangle))
print(hasattr(Rectangle, 'set_coords'))
print(hasattr(Rectangle, 'get_coords'))
print(hasattr(Rectangle, 'draw'))
print(rect.get_coords())
rect.draw()

rect2 = Rectangle(Point(0, 0), Point(1, 1))
print(rect2.get_coords())
rect2.draw()
