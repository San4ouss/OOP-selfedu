class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_point(self, x, y, speed):
        self.track.append([(x, y), speed])

    def check_indx(self, indx):
        if indx < 0 or indx >= len(self.track):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.check_indx(item)

        return self.track[item]

    def __setitem__(self, key, value):
        self.check_indx(key)

        self.track[key][1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

# res = tr[3]  # IndexError
