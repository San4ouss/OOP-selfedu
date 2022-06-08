lst_in = ["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"]  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы

    def insert(self, data):
        # for i in [i.split() for i in data]:
        #     d = {}
        #     for key, value in zip(self.FIELDS, i):
        #         d[key] = value
        #     self.lst_data.append(d)

        for i in data:
            # self.lst_data.append({key: value for key, value in zip(self.FIELDS, i.split())})
            self.lst_data.append((dict(zip(self.FIELDS, i.split()))))
            # print(*zip(self.FIELDS, i.split()))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)

lst = [i.split() for i in lst_in]
print(lst)
print(db.select(0, 5))
