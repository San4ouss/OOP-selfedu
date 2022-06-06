class Translator:
    d = {}

    def add(self, eng, rus):
        if eng in self.d.keys():
            self.d[eng] += [rus]
        else:
            self.d[eng] = [rus]

    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        return self.d[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))

print(Translator.d)
print(tr.translate('tree')[0])
