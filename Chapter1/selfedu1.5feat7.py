class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots

    def get_config(self):
        # return [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
        #         f'Слотов памяти: {self.total_mem_slots}',
        #         f'Память: {"; ".join([i.name + " - " + str(i.volume) for i in self.mem_slots])}'
        #         ]

        return [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {"; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])}'
                ]


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
mb.get_config()

print(mb.get_config())
