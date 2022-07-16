class Model:
    def __init__(self):
        self.d = None

    def query(self, **kwargs):
        self.d = kwargs

    def __str__(self):
        return f'''Model: {', '.join([f"{key} = {value}" for key, value in self.d.items()])}''' if self.d else "Model"


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
print("Model: id = 1, fio = Sergey, old = 33")
model2 = Model()
model2.query()
print(model2)
