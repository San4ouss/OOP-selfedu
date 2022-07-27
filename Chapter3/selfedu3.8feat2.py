class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__all_attributes_len = len(kwargs)
        self.__keys = tuple(kwargs.keys())

    def __check_item(self, item):
        if type(item) is not int or not (-self.__all_attributes_len <= item < self.__all_attributes_len):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__check_item(item)
        return getattr(self, self.__keys[item])

    def __setitem__(self, key, value):
        self.__check_item(key)
        setattr(self, self.__keys[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')

r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[1])  # Супер курс по ООП
# r[3]  # генерируется исключение IndexError
