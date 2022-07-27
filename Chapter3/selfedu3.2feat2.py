from random import randint


# решение с помощью метода __call__
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        lst = [self.psw_chars[randint(0, len(self.psw_chars) - 1)]
               for i in range(randint(self.min_length, self.max_length + 1))]
        return "".join(lst)


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for i in range(3)]

print(lst_pass)

# # решение с помощью замыкания
# def RandomPassword(psw_chars, min_length, max_length):
#     def wrapper():
#         return "".join([psw_chars[randint(0, len(psw_chars) - 1)] for i in range(randint(min_length, max_length + 1))])
#
#     return wrapper
#
#
# rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
# lst_pass = [rnd() for i in range(3)]
#
# print(lst_pass)
