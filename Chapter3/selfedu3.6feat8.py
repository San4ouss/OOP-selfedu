class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __setattr__(self, key, value):
        if key in ("name", "author") and not isinstance(value, str):
            raise AttributeError("Локальные свойства name и author должны иметь тип str")
        if key == "year" and not isinstance(value, int):
            raise AttributeError("Локальное свойство year должно иметь тип int")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Python; Балакирев С.М.; 2020",
          "Python ООП; Балакирев С.М.; 2021",
          "Python ООП; Балакирев С.М.; 2022",
          "Python; Балакирев С.М.; 2021"]

lst_bs = [BookStudy(i[0], i[1], int(i[2])) for i in [[x.strip() for x in row.split(";")] for row in lst_in]]

unique_books = 0
for i in range(1, len(lst_bs)):
    if lst_bs[i] != lst_bs[i - 1]:
        unique_books += 1

# lst_bs = [BookStudy(*line.split('; ')) for line in lst_in]
# unique_books = len(set(map(hash, lst_bs)))
print(unique_books)
