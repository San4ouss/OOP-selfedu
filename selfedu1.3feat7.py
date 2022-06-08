class Dictionary:
    rus: str = "Питон"
    eng: str = "Python"


# try:
#     print(getattr(Dictionary, "rus_word"))
# except AttributeError:
#     print(False)

print(getattr(Dictionary, 'rus_word', False))
