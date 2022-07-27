class Handler:
    def __init__(self, methods=("GET",)):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if request.get('method') in self.__methods or request.get('method') is None:
                return self.post(func, request) if request.get('method') == "POST" else self.get(func, request)
            else:
                return None

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


# @Handler(methods=('GET', 'POST'))
# def contact(request):
#     return "контакты"
#
#
# res = contact({"method": "POST", "url": "contact.html"})
# print(res)

assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"


@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"


assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"


@Handler(methods=('POST'))
def index(request):
    return "index"


assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
