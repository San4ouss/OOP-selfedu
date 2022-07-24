class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.data = []

    def write(self, record):
        self.data.append(record)

    def read(self, pk):
        pass


class Record:
    pk = 0

    def __new__(cls, *args, **kwargs):
        cls.pk += 1
        return object.__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.descr.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)
