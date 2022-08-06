from random import randint

class Cpu:
    
    draws = 0

    def __init__(self):
        self._name = "CPU"
        self._symbol = ""
        self._wins = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol

    def get_wins(self):
        return self._wins

    def set_wins(self, wins):
        self._wins = wins
    
    def get_random_pos(self):
        return randint(0, 8)
