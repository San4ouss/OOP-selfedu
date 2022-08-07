class Cell:
    def __init__(self):
        self.__value = 0
        self.is_free = True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        # if self.is_free:
        #     raise ValueError('клетка уже занята')
        self.is_free = False
        self.__value = value

    def __bool__(self):
        return bool(self.is_free)


class TicTacToe:
    def __init__(self):
        self.pole = [tuple([Cell() for _ in range(3)]) for _ in range(3)]

    def clear(self):
        self.__init__()

    @staticmethod
    def check_indx(indx):
        if isinstance(indx[0], int) and isinstance(indx[1], int):
            if len(indx) != 2 or indx[0] >= 3 or indx[1] >= 3:
                raise IndexError('неверный индекс клетки')

    def check_is_free(self, indx1, indx2):
        if bool(self.pole[indx1][indx2].value):
            raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        self.check_indx(item)

        if isinstance(item[1], slice):
            return tuple([i.value for i in self.pole[item[0]]])
        elif isinstance(item[0], slice):
            return tuple([i[item[1]].value for i in self.pole])
        else:
            return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.check_indx(key)

        if isinstance(key[1], slice):
            for i in range(len(value)):
                self.check_is_free(key[0], i)
                self.pole[key[0]][i].value = value[i]
        elif isinstance(key[0], slice):
            for i in range(len(self.pole)):
                self.check_is_free(i, key[0])
                self.pole[i][key[0]].value = value[i]
        else:
            self.check_is_free(key[0], key[1])
            self.pole[key[0]][key[1]].value = value

# game = TicTacToe()
# game.clear()
# game[0, 0] = 1
# game[1, 0] = 2
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# game[3, 2] = 2  # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0
#
# print(v1)
# print(v2)
#
# for i in game.pole:
#     for j in i:
#         print(j.value, j.is_free, end=" ")
#     print()


# g = TicTacToe()
# g.clear()
# assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
# g[1, 1] = 1
# g[2, 1] = 2
# assert g[1, 1] == 1 and g[
#     2, 1] == 2, "неверно отработала операция " \
#                 "присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"
#
# try:
#     res = g[3, 0]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
#
# try:
#     g[3, 0] = 5
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"
#
# g.clear()
# g[0, 0] = 1
# g[1, 0] = 2
# g[2, 0] = 3
#
# assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
#     1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
#
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
# res = cell.is_free
# cell.is_free = True
# assert bool(cell), "функция bool вернула False для свободной клетки"
