class Board:

    def __init__(self):
        self._type = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
        ]
        self._runs = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]

    def reset(self):
        self._type = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
        ]

    def display(self):
        counter = 0
        self._runs = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]

        for a, b, c in self._runs:
            print(f"    {a + 1} | {b + 1} | {c + 1}    {self._type[a]} | {self._type[b]} | {self._type[c]}")

            if counter < 2:
                print("   -----------  -----------") 
                counter += 1

        print()
       
    def _is_position_empty(self, *args):
        pos = args[0]

        if self._type[pos] == " ":
            return True
                
        return False

    def update_pos(self, p_symbol):
        position = 15

        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self._is_position_empty(position - 1): 
            position = int(input("Choose a number between 1-9: "))

        self._type[position -1] = p_symbol

    def check_winner(self, p_symbol):
        runs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
                [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
                [0, 4, 8], [2, 4, 6]             # diagonal
        ]

        for a, b, c in runs:
            if self._type[a] == self._type[b] == self._type[c] == p_symbol:
                return True
                    
        return False
  
    def is_full(self):
        for i in self._type:
            if i == " ":
                return False

        return True
