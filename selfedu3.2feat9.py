class InputDigits:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.__fn().split()))


@InputDigits
def input_dg():
    return input()


# input_dg = InputDigits(input)

res = input_dg()

print(res)
