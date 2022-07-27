class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise AttributeError("Локальные свойства должны иметь тип int или float")
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)


s_inp = input()

# lst = [[float(i) for i in row.split()] for row in s_inp.split(";")]
# print(lst)
# lst_dims = [Dimensions(*i) for i in lst]
# print(lst_dims)

lst_dims = []
for i in s_inp.split(";"):
    args = (float(j) for j in i.strip().split())
    lst_dims.append(Dimensions(*args))

lst_dims = sorted(lst_dims, key=hash)

print(lst_dims)

for i in lst_dims:
    print(hash(i))
