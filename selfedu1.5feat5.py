class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            return 1
        elif self.c >= self.a + self.b or self.a >= self.b + self.c or self.b >= self.a + self.c:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
