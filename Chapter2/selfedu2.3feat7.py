class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if isinstance(string, str) and self.min_length <= len(string) <= self.max_length:
            return True
        return False


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "-" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        for i in ["<form>", f"Логин: {self.login}", f"Пароль: {self.password}", f"Email: {self.email}", "</form>"]:
            print(i)


st = RegisterForm("alex", "12345", "a12@mail.ru")
print(st.get_fields())
st.show()
