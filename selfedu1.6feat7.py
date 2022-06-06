from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class Base:
    def __init__(self, name, size=10):
        if TextInput.check_name(name):
            self.name = name
            self.size = size

        else:
            raise ValueError('некорректное имя поля')

    @classmethod
    def check_name(cls, name):
        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьъэюя " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        if len(name) > 50 or len(name) < 3:
            return False
        for i in name:
            if i not in CHARS_CORRECT:
                return False
        else:
            return True


class TextInput(Base):
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Base):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)
