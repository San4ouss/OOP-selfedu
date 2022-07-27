from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return True if self.min_length <= len(args[0]) <= self.max_length else False


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        for i in args[0]:
            if i not in self.chars:
                return False
        else:
            return True


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")

lv = LengthValidator(3, 50)
cv = CharsValidator(ascii_lowercase + digits)
print(lv("ghlrjwjrwrj123"))
print(cv("ettretet32424."))
