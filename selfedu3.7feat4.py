class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise AttributeError("Локальное свойство name должно иметь тип str")
        if key in ("old", "score") and type(value) is not int:
            raise AttributeError("Локальные свойства old и score должны иметь тип int")
        object.__setattr__(self, key, value)

    def __bool__(self):
        return bool(self.score)


lst_in = ["Балакирев; 34; 2048",
          "Mediel; 27; 0",
          "Влад; 18; 9012",
          "Nina P; 33; 0"]

players = []
for i in lst_in:
    players.append(Player(i.split("; ")[0], int(i.split("; ")[1]), int(i.split("; ")[2])))

players_filtered = list(filter(bool, players))

print(players_filtered)
