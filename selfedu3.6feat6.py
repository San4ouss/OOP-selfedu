from collections import Counter


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.total = 1

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Локальное свойство name должно иметь тип str")
        if key in ("weight", "price") and not isinstance(value, (int, float)):
            raise AttributeError("Локальные свойства weight, price должны иметь тип int или float")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Системный блок: 1500 75890.56",
          "Монитор Samsung: 2000 34000",
          "Клавиатура: 200.44 545",
          "Монитор Samsung: 2000 34000"]

# lst = [[j.strip() for j in i.split(":")] for i in lst_in]
# print(lst)
# print(lst[0][1].split())

shop_items = {ShopItem(i[0], float(i[1].split()[0]), float(i[1].split()[1])): []
              for i in [[j.strip() for j in i.split(":")] for i in lst_in]}

shop_items = {key: [key, key.total] for key in shop_items.keys()}

# items = []
# for line in lst_in:
#     name, data = line.split(':')
#     weight, price = map(float, data.split())
#     items.append(ShopItem(name, weight, price))
#
# shop_items = {k: [k, v] for k, v in Counter(items).items()}

# print(shop_items)
