# import re

# lst = [1, 2, 3, "python", True]
# print(lst[::-1])
# lst.reverse()
# print(lst)

# array1 = [1, 3, 8, 15, 32]
# array2 = [1, 2, 3]
# array3 = [i for i in array1 if i in array2]
# print(array3)
#
# array4 = set(array1) & set(array2)
# print(list(array4))

# #  регулярные выражения
# number = "1234-5678-9012-0000"
# name = "SERGEI BALAKIREV"

# match = re.findall(r"[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]", number)
# match2 = re.match(r"\d{4}-\d{4}-\d{4}-\d{4}", number)
# print(match)
# print(match2)
# if match2:
#     print("correct number")
# else:
#     print("bad number")

# match_n = re.findall(r"^[A-Z]+ [A-Z]+$", name)
# match_n2 = re.match(r"[A-Z]+ [A-Z]+", name)
# print(match_n)
# print(match_n2)
# if match_n2:
#     print("correct name")
# else:
#     print("bad name")
#
# print(name == name.strip())
# print(name.strip())

# print(0 <= 10.0 <= 1000)

# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         pass
#
#
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
#
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr

# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     a = Integer()
#     b = Integer()
#     c = Integer()
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     def __setattr__(self, key, value):
#         if value > self.MAX_DIMENSION or value < self.MIN_DIMENSION:
#             return None
#         elif key in ("MIN_DIMENSION", "MAX_DIMENSION"):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         else:
#             object.__setattr__(self, key, value)

# filter_slots = [None, None, None]
# print(len(filter_slots))

# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ('jpg', 'bmp', 'jpeg')
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

# a = filter(lambda x: isinstance(x, str), [1, "2", 3, "4"])
# print(list(a))

# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# for i in lst:
#     print(f'''<ul>
#     <li>Пункт меню 1</li>
#     <li>Пункт меню 2</li>
#     <li>Пункт меню 3</li>
#     </ul>''')

# print(f'''<ul> {" ".join([f'<li>{i}</li>' for i in lst])} </ul>''')


# values = {'id': 1, 'fio': 'Sergey', 'old': 33}
# a = " ".join([f"{key}={value}" for key, value in values.items()])
# print(a)


# lst1 = [1, 0, True, False, 5.0, True, 1, True, -7.87]
# lst2 = [10, True, False, True, 1, 7.87]

# lst1 = [1, 2, 2, 3, 3]
# lst2 = [2, 3]
#
# new_lst1 = [(i, type(i)) for i in lst1]
# new_lst2 = [(i, type(i)) for i in lst2]

# print(lst1)
# print(lst2)
# res = [i[0] for i in lst1 if i not in lst2]
# print(res)


# for i in new_lst1:
#     if i in new_lst2:
#         print(i)
#         new_lst1.remove(i)
#         new_lst2.remove(i)
#
# print([i[0] for i in new_lst1])

# if (False, bool) in new_lst2:
#     print("found")
# else:
#     print("not found")

# res = []
# for i in new_lst1:
#     if i not in new_lst2:
#         res.append(i[0])
#     else:
#         new_lst2.remove(i)
#
# print(new_lst2)
# print(res)


s = {'txt', 'doc', 'xls', 'png', 'jpeg', 'jpg'}
print(s)
print('doc' in s)
