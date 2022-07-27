class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        try:
            return bool(sum([self.x1, self.y1, self.x2, self.y2]))
        except AttributeError:
            return False

    def get_coords(self):
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for i in lst_geom:
    if bool(i):
        i.get_coords()
