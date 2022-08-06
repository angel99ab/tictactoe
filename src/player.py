class Player:

    draws = 0

    def __init__(self):
        self.__name = ""
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

    def is_valid_name(self):
        if len(self.__name) == 0 or len(self.__name) > 11:
            return False
        
        return True
