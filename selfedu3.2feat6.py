class RenderList:
    def __init__(self, type_list):
        if type_list not in ("ul", "ol"):
            self.type_list = "ul"
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        return f'''<{self.type_list}> {" ".join([f'<li>{i}</li>' for i in args[0]])} </{self.type_list}>'''


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
