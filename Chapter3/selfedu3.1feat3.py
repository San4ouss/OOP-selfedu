class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ("title", "author") and isinstance(value, str):
            return object.__setattr__(self, key, value)
        elif key in ("pages", "year") and isinstance(value, int):
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)

book2 = Book("Python ООП", "Сергей Балакирев", "123", 2022)
