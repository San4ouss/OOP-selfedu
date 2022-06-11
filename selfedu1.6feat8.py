TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        global TYPE_OS
        if TYPE_OS == 1:
            instance = super().__new__(DialogWindows)
            setattr(instance, "name", args[0])
            return instance
        elif TYPE_OS == 2:
            instance = super().__new__(DialogLinux)
            setattr(instance, "name", args[0])
            return instance
        else:
            return super().__new__(cls)

    def __init__(self, name):
        self.name = name


w1 = Dialog("w1")
print(isinstance(w1, DialogWindows))
print(w1.name)
print(type(w1))
l1 = Dialog("l1")
print(isinstance(l1, DialogLinux))
print(l1.name)
print(type(l1))
d1 = Dialog("d1")
print(isinstance(d1, Dialog))
print(type(d1))
print(d1.name)
