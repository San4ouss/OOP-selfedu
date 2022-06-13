import math


class PathLines:
    def __init__(self, *args):
        if args:
            self.lst = list(args)
            self.lst.insert(0, LineTo(0, 0))
        else:
            self.lst = list()

    def get_path(self):
        return self.lst

    def get_length(self):
        return sum([math.sqrt((self.lst[i].x - self.lst[i - 1].x) ** 2 + (self.lst[i].y - self.lst[i - 1].y) ** 2)
                    for i in range(1, len(self.lst))])

    def add_line(self, line):
        self.lst.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

print(dist)

p1 = PathLines()
print(p1.get_path())

p2 = PathLines(LineTo(10, 20), LineTo(10, 30))
print(p2.get_path())
print(p2.get_length())
