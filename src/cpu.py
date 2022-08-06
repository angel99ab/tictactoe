from random import randint

class Cpu:
    
    draws = 0

    def __init__(self):
        self.__name = "CPU"
        self.__symbol = ""
        self.__wins = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_symbol(self):
        return self.__symbol

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def get_wins(self):
        return self.__wins

    def set_wins(self, wins):
        self.__wins = wins
    
    def get_random_pos(self):
        return randint(0, 8)
