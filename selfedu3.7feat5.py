import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        # lst_in = ["sc_lib@list.ru; От Балакирева; Успехов в IT!",
        #           "mail@list.ru; Выгодное предложение; Вам одобрен кредит.",
        #           "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."]
        for i in lst_in:
            self.inbox_list.append(MailItem(*i.split("; ")))


class MailItem:
    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def __setattr__(self, key, value):
        if key in ("mail_from", "title", "content") and not isinstance(value, str):
            raise AttributeError("Локальные свойства должны иметь тип str")
        object.__setattr__(self, key, value)

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return bool(self.is_read)


mail = MailBox()
mail.receive()

for i in range(0, len(mail.inbox_list), len(mail.inbox_list) - 1):
    mail.inbox_list[i].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))

# for i in mail.inbox_list:
#     print(i.is_read)

# print(inbox_list_filtered)
