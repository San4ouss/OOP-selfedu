class Handler:
    def __init__(self, methods=("GET",)):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            pass

        return wrapper
