import string
import random


class EmailValidator:
    symbols = string.ascii_letters + "1234567890_.@"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count("@") > 1 or email.count("@") == 0:
            return False
        elif email.find("@") > 100 or len(email) - 1 - email.find("@") > 50:
            return False
        elif email.find("@") > email.find(".", email.find("@")):
            return False
        elif email.find("..") != -1:
            return False
        for i in email:
            if i not in cls.symbols:
                return False
        else:
            return True

    @classmethod
    def get_random_email(cls):
        random_email = ""
        for i in range(random.randint(1, 99)):
            random_email += random.choice(cls.symbols[:-1])

        return random_email + "@gmail.com"

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


res1 = EmailValidator.check_email("sc_lib@list.ru")  # True
res2 = EmailValidator.check_email("sc_lib@list_ru")  # False

assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
