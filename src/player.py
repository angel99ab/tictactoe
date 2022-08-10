class Player:

    draws = 0

    def __init__(self, symbol):
        self._symbol = symbol
        self._wins = 0

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol

    def get_wins(self):
        return self._wins

    def set_wins(self, wins):
        self._wins = wins
