class HandlerGET:
    def get(self, func, request, *args, **kwargs):
        self.func = func
        self.request = request





@HandlerGET
def contact(request):
    return "Сергей Балакирев"