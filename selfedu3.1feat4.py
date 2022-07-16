class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return object.__new__(cls)

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.id

    def __setattr__(self, key, value):
        if (key == "name" and isinstance(value, str)) or (
                key in ("weight", "price", "id") and isinstance(value, (int, float)) and value >= 0):
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        return object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

book1 = Product("Python ООП", 100, 1024)
book2 = Product("Python", 100, 1024)
book3 = Product("ООП", 100, 1024)
print(book1.id)
print(book2.id)
print(book3.id)
print(book1.__dict__)
print(Product.__dict__)
