class SmartPhone:
    def __init__(self, model: str):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for i in self.apps:
            if app.name == i.name:
                break
        else:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)

    def __setattr__(self, key, value):
        if key == "model" and not isinstance(value, str):
            raise TypeError("Модель должна быть строкой")
        return object.__setattr__(self, key, value)


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        return object.__setattr__(self, key, value)


class AppYouTube:
    def __init__(self, max_memory, name="YouTube"):
        self.max_memory = max_memory
        self.name = name


class AppPhone:
    def __init__(self, phone_list, name="Phone"):
        self.phone_list = phone_list
        self.name = name


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)

print(sm.apps)
