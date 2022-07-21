stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


lst = [[i.strip("–?!,.;") for i in line.split() if len(i.strip("–?!,.;")) > 0] for line in stich]
lst_text = [StringText(i) for i in lst]
lst_text_sorted = [" ".join(i.lst_words) for i in sorted(lst_text, reverse=True)]

for i in lst_text_sorted:
    print(i)

print(lst_text_sorted)
