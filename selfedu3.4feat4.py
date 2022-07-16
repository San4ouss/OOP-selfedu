class NewList:
    def __init__(self, *args):
        if len(args) == 0:
            self.__lst = []
        else:
            self.__lst = args[0]

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Правый операнд должен иметь тип list или NewList")
        if isinstance(other, NewList):
            sc = [(i, type(i)) for i in other.__lst]
        else:
            sc = [(i, type(i)) for i in other]
        new__lst = [(i, type(i)) for i in self.__lst]

        result = []
        for i in new__lst:
            if i not in sc:
                result.append(i[0])
            else:
                sc.remove(i)

        return NewList(result)

    def __rsub__(self, other):
        return NewList(other) - self
        # if not isinstance(other, (list, NewList)):
        #     raise ArithmeticError("Правый операнд должен иметь тип list")
        # if isinstance(other, NewList):
        #     sc = [(i, type(i)) for i in other.__lst]
        # else:
        #     sc = [(i, type(i)) for i in other]
        # new__lst = [(i, type(i)) for i in self.__lst]
        #
        # result = []
        # for i in sc:
        #     if i not in new__lst:
        #         result.append(i[0])
        #     else:
        #         new__lst.remove(i)
        #
        # return NewList(result)

    def get_list(self):
        return self.__lst


lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
