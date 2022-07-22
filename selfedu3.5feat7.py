class FileAcceptor:
    def __init__(self, *args):
        self.tags = args[0] if len(args) == 1 else list(args)

    def __call__(self, *args, **kwargs):
        if args[0].split(".")[-1] in self.tags:
            return True
        return False

    def __add__(self, other):
        return FileAcceptor(tuple(set(self.tags) | set(other.tags)))
        # return FileAcceptor(set(list(self.tags) + list(other.tags)))

    def __radd__(self, other):
        return self + other


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
print(acceptor12.tags)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor(["txt", "doc", "xls"])
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)

filenames2 = list(filter(acceptor_images, filenames))
print(filenames2)
