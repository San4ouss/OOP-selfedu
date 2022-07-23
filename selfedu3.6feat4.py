class Rect:
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def __eq__(self, other):
        return self.wight == other.wight and self.height == other.height

    def __hash__(self):
        return hash((self.wight, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2

print(h1 == h2)
