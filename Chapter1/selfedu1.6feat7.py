class SingletonFive:
    __instance = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__instance = super().__new__(cls)
        cls.__counter += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

print(objs)
