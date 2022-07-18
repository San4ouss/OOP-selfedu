class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.__fn, request) if request.get("method") in ("GET", None) else None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET"})
# assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
# res = contact({"method": "POST"})
# assert res is None, "декорированная функция вернула неверные данные"
# res = contact({"method": "POST2"})
# assert res is None, "декорированная функция вернула неверные данные"
#
# res = contact({})
# assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"

print(res)
