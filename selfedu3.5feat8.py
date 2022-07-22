class Money:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        if self.__cb is None:
            raise ValueError("Неизвестен курс валют.")
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @staticmethod
    def check_currency(other):
        if isinstance(other, MoneyD):
            return other.volume * other.cb.rates.get("rub")

        elif isinstance(other, MoneyE):
            return other.volume * other.cb.rates.get("rub") * other.cb.rates.get("euro")

        else:
            return other.volume

    def __eq__(self, other):
        first_currency = self.check_currency(self)
        second_currency = self.check_currency(other)
        return 0 <= abs(first_currency - second_currency) <= 0.1

    def __lt__(self, other):
        first_currency = self.check_currency(self)
        second_currency = self.check_currency(other)
        return second_currency - first_currency > 0.1

    def __le__(self, other):
        first_currency = self.check_currency(self)
        second_currency = self.check_currency(other)
        return second_currency - first_currency >= 0.1


class MoneyR(Money):
    def __init__(self, volume=0):
        super().__init__(volume)


class MoneyD(Money):
    def __init__(self, volume=0):
        super().__init__(volume)


class MoneyE(Money):
    def __init__(self, volume=0):
        super().__init__(volume)


class CentralBank:
    rates = {}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = CentralBank


rubles = MoneyR()
print(type(rubles.__class__.__name__))

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
