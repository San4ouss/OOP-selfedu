class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def check_right_operand(other):
        if isinstance(other, (int, float)):
            return other
        else:
            return other.ro * other.volume

    def __eq__(self, other):
        sc = self.check_right_operand(other)
        return self.ro * self.volume == sc

    def __lt__(self, other):
        sc = self.check_right_operand(other)
        return self.ro * self.volume < sc

    def __le__(self, other):
        sc = self.check_right_operand(other)
        return self.ro * self.volume <= sc


body1 = Body("John", 10, 20)
body2 = Body("Jim", 20, 10)
print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2)  # True, если масса тела body1 равна массе тела body2
print(body1 < 10)  # True, если масса тела body1 меньше 10
print(body2 == 5)  # True, если масса тела body2 равна 5
