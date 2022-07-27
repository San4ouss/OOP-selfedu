class Notes:
    uid: int = 1005435
    title: str = "Шутка"
    author: str = "И.С. Бах"
    pages: int = 2


print(getattr(Notes, "author"))
