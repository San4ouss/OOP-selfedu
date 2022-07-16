# #  feat 1
# def func_show(func):
#     def wrapper(*args, **kwargs):
#         print(f"Площадь прямоугольника: {func(*args, **kwargs)}")
#
#     return wrapper
#
#
# @func_show
# def get_sq(width, height):
#     return width * height
#
#
# get_sq(8, 11)


# #  feat 2
# def show_menu(func):
#     def wrapper(*args, **kwargs):
#         for i, j in enumerate(func(*args, **kwargs), start=1):
#             print(f"{i}. {j}")
#
#     return wrapper
#
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
#
# get_menu("Главная Добавить Удалить Выйти")


# #  feat 3
# def get_sort_list(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args, **kwargs))
#
#     return wrapper
#
#
# @get_sort_list
# def get_list(s):
#     return list(map(int, s.split()))
#
#
# lst = get_list(input())
# print(*lst)


# #  feat 4
# def get_dict(func):
#     def wrapper(*args, **kwargs):
#         lst = func(*args, **kwargs)
#         return dict(zip(lst[0], lst[1]))
#
#     return wrapper
#
#
# @get_dict
# def get_list(s1, s2):
#     return s1.split(), s2.split()
#
#
# d = get_list(input(), input())
# print(*sorted(d.items()))


#  feat 5
