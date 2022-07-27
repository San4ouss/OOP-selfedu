import random


class Geom:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Geom):
    pass


class Rect(Geom):
    pass


class Ellipse(Geom):
    pass


classes = [Line, Rect, Ellipse]
elements = [classes[random.randint(0, 2)](random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
                                          random.randint(0, 100)) for i in range(217)]

for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)

# проверка
print(len(elements))
for i in elements:
    if isinstance(i, Line):
        print(i.sp, i.ep)
