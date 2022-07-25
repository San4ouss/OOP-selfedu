class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if obj else None


class Record:
    pk_counter = 0

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__counter()

    @classmethod
    def __counter(cls):
        cls.pk_counter += 1
        return cls.pk_counter

    def __setattr__(self, key, value):
        if key in ("fio", "descr") and not isinstance(value, str):
            raise AttributeError("Локальные свойства fio и descr должны иметь тип str")
        if key == "old" and not isinstance(value, int):
            raise AttributeError("Локальное свойство old должно иметь тип int")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Балакирев С.М.; программист; 33",
          "Кузнецов А.В.; разведчик-нелегал; 35",
          "Суворов А.В.; полководец; 42",
          "Иванов И.И.; фигурант всех подобных списков; 26",
          "Балакирев С.М.; преподаватель; 37"]

db = DataBase("123")
for i in lst_in:
    fio, descr, old = i.split(";")
    db.write(Record(fio.strip(), descr.strip(), int(old)))

# print(db.dict_db)
