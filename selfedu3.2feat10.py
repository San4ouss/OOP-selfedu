class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))

        return wrapper


class RenderDigit:

    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None


@InputValues(RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)

# render = RenderDigit()
# d1 = render("123")  # 123 (целое число)
# d2 = render("45.54")  # None (не целое число)
# d3 = render("-56")  # -56 (целое число)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")  # None (не целое число)
# print(d1, d2, d3, d4, d5, sep="\n")
