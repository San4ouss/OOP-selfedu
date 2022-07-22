class Money:
    d = {"MoneyR": "rus", "MoneyD": "dollar", "MoneyE": "euro"}

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
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __eq__(self, other):
        if isinstance(self, MoneyR):
            rubles = self.__cb.rates.get("rub") * self.__volume
            currency = other.__cb.rates.get("rub") * other.__cb.rates.get(
                other.d[other.__class__.__name__]) * other.volume
            return rubles == currency
        else:
            currency1 = self.__cb.rates.get("rub") * self.__cb.rates.get(
                other.d[other.__class__.__name__]) * self.volume
            currency2 = other.__cb.rates.get("rub") * other.__cb.rates.get(
                other.d[other.__class__.__name__]) * other.volume
            return currency1 == currency2

    def __lt__(self, other):
        rubles = self.__cb.rates.get("rub") * self.__volume
        currency = other.__cb.rates.get("rub") * other.__cb.rates.get(other.d[other.__class__.__name__]) * other.volume
        return rubles < currency

    def __le__(self, other):
        rubles = self.__cb.rates.get("rub") * self.__volume
        currency = other.__cb.rates.get("rub") * other.__cb.rates.get(other.d[other.__class__.__name__]) * other.volume
        return rubles <= currency


class MoneyR(Money):
    def __init__(self, volume=0):
        super().__init__(volume)

    def __eq__(self, other):
        if isinstance(self, MoneyR):
            rubles = self.__cb.rates.get("rub") * self.__volume
            currency = other.__cb.rates.get("rub") * other.__cb.rates.get(
                other.d[other.__class__.__name__]) * other.volume
            return rubles == currency
        else:
            currency1 = self.__cb.rates.get("rub") * self.__cb.rates.get(
                other.d[other.__class__.__name__]) * self.volume
            currency2 = other.__cb.rates.get("rub") * other.__cb.rates.get(
                other.d[other.__class__.__name__]) * other.volume
            return currency1 == currency2

    def __lt__(self, other):
        rubles = self.__cb.rates.get("rub") * self.__volume
        currency = other.__cb.rates.get("rub") * other.__cb.rates.get(other.d[other.__class__.__name__]) * other.volume
        return rubles < currency

    def __le__(self, other):
        rubles = self.__cb.rates.get("rub") * self.__volume
        currency = other.__cb.rates.get("rub") * other.__cb.rates.get(other.d[other.__class__.__name__]) * other.volume
        return rubles <= currency


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
