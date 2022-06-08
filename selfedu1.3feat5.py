class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "О111АА77")

# print(Car.color)
print(Car.__dict__['color'])
