from math import sqrt


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_track(self, tr):
        self.points.append(tr)

    def get_tracks(self):
        return tuple(self.points)

    @staticmethod
    def count_length(other):
        x_start = other.start_x
        y_start = other.start_y
        length = 0
        for i in other.points:
            length += sqrt((i.to_x - x_start) ** 2 + (i.to_y - y_start) ** 2)
            x_start = i.to_x
            y_start = i.to_y
        return length

    def __len__(self):
        return int(self.count_length(self))

    def __eq__(self, other):
        return self.count_length(self) == self.count_length(other)

    def __lt__(self, other):
        return self.count_length(self) < self.count_length(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

print(res_eq)
print(len(track1))
print(len(track2))
