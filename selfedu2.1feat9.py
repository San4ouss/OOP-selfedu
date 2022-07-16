class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, obj):
        self.__next = obj

    def get_prev(self):
        return self.__prev

    def set_prev(self, obj):
        self.__prev = obj

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        pass

    def remove_obj(self):
        pass

    def get_data(self):
        pass


ob = ObjList("данные 1")
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
print(res)
