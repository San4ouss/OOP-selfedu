class Viber:
    lst = []

    @classmethod
    def add_message(cls, msg):
        cls.lst.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.lst.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = True

    @classmethod
    def show_last_message(cls, number):
        return cls.lst[number].text

    @classmethod
    def total_messages(cls):
        return len(cls.lst)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

print(Viber.show_last_message(0))
print(Viber.total_messages())


