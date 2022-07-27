class Cell:
    pole = []

    def __init__(self, around_mines, mine, fl_open=False):
        self.around_mine = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        pass
