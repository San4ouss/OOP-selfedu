class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return object.__setattr__(self, key, value)

    def __lt__(self, other):
        return self.__a * self.__b * self.__c < other.__a * other.__b * other.__c

    def __le__(self, other):
        return self.__a * self.__b * self.__c <= other.__a * other.__b * other.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem("кеды", 1024, Dimensions(40, 30, 120)), ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
            ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
            ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

for i in lst_shop_sorted:
    print(f"name: {i.name}, volume: ({i.dim.a}, {i.dim.b}, {i.dim.c})")
