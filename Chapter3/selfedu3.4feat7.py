class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
        elif type(other) == int:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


lib = Lib()
book = Book("title", "author", 2022)
book2 = Book("title2", "author2", 2022)
book3 = Book("title3", "author3", 2022)

lib = lib + book
lib += book2
lib += lib + book3

# lib = lib - book3
# lib -= book
lib = lib - 0

print(len(lib))
print(lib.book_list)
