class Board:

    def __init__(self):
        self.__number = 0
        self.__type = None
        self.__runs = []

    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number
    
    def get_type(self):
        return self.__type
    
    def set_type(self, type):
        self.__type = type
    
    def reset(self):
        if self.__number in [1, 2]:
            self.__type = [
                            " ", " ", " ",
                            " ", " ", " ",
                            " ", " ", " "
            ]
        if self.__number in [3, 4]:
            self.__type = [
                            [" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
            ]

    def show_types(self):
        print("\n  1) Simple ASC    2) Simple DES    3) Column/Row      4) Column/Row \n")
        print("     7 | 8 | 9        1 | 2 | 3        11 | 12 | 13       1a | 1b | 1c   ")
        print("    -----------      -----------      --------------     --------------  ")
        print("     4 | 5 | 6        4 | 5 | 6        21 | 22 | 23       2a | 2b | 2c   ")
        print("    -----------      -----------      --------------     --------------  ")
        print("     1 | 2 | 3        7 | 8 | 9        31 | 32 | 33       3a | 3b | 3c \n")

    def display(self):
        if self.__number == 1:
            self.__runs = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
            self.__first()
        elif self.__number == 2:
            self.__runs = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            self.__first()
        elif self.__number == 3:
            self.__third()
        elif self.__number == 4:
            self.__fourth()

    def __first(self):
        counter = 0

        for a, b, c in self.__runs:
            print(f"    {a + 1} | {b + 1} | {c + 1}    {self.__type[a]} | {self.__type[b]} | {self.__type[c]}")

            if counter < 2:
                print("   -----------  -----------") 
                counter += 1

        print()
    
    def __third(self):
        row = 0
        column = 0
        n = 10

        for i in range(3):
            print(f"    {n + 1} | {n + 2} | {n + 3}      {self.__type[row][column]} | {self.__type[row][column + 1]} | {self.__type[row][column + 2]}")

            if i < 2:
                print("   --------------    -----------") 

            row += 1
            n += 10

        print()

    def __fourth(self):
        print("    1a | 1b | 1c      " + self.__type[0][0] + " | " + self.__type[0][1] + " | " + self.__type[0][2])
        print("   --------------    -----------")
        print("    2a | 2b | 2c      " + self.__type[1][0] + " | " + self.__type[1][1] + " | " + self.__type[1][2])
        print("   --------------    -----------")
        print("    3a | 3b | 3c      " + self.__type[2][0] + " | " + self.__type[2][1] + " | " + self.__type[2][2])
        print()
    
    def __is_position_empty(self, *args):
        pos = row = args[0]

        if len(args) == 2:
            column = args[1]

        if self.__number in [1, 2]:
            if self.__type[pos] == " ":
                return True

        if self.__number == 3:
            if self.__type[row][column] == " ":
                return True

        if self.__number == 4:
            if column == "a":
                column = 0
            if column == "b":
                column = 1
            if column == "c":
                column = 2
            if self.__type[row][column] == " ":
                return True
                
        return False

    def update_pos(self, p_symbol):
        if self.__number in [1, 2]:
            position = 15

            while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.__is_position_empty(position - 1): 
                position = int(input("Choose a number between 1-9: "))

            position -= 1

            if self.__is_position_empty(position):
                self.__type[position] = p_symbol
        if self.__number == 3:
            row = 15
            column = 15

            while (row or column) not in [1, 2, 3] or not self.__is_position_empty(row - 1, column - 1): 
                row = int(input("row: "))
                column = int(input("column: "))
            
            row -= 1
            column -= 1

            if self.__is_position_empty(row, column):
                self.__type[row][column] = p_symbol
        if self.__number == 4:
            row = 15
            column = "f"

            while row not in [1, 2, 3] or column not in ["a", "b", "c"] or not self.__is_position_empty(row - 1, column): 
                row = int(input("row: "))
                column = input("column: ")

            if column == "a":
                column = 1
            if column == "b":
                column = 2
            if column == "c":
                column = 3

            row -= 1
            column -= 1

            if self.__is_position_empty(row, column):
                self.__type[row][column] = p_symbol

    def check_winner(self, p_symbol):
        runs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
                [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
                [0, 4, 8], [2, 4, 6]             # diagonal
        ]

        if self.__number in [1, 2]:
            for a, b, c in runs:
                if self.__type[a] == self.__type[b] == self.__type[c] == p_symbol:
                    return True
                    
            return False

        if self.__number in [3, 4]:
            # check rows
            if self.__type[0][0] == self.__type[0][1] == self.__type[0][2] == p_symbol:
                return True
        
            if self.__type[1][0] == self.__type[1][1] == self.__type[1][2] == p_symbol:
                return True
            
            if self.__type[2][0] == self.__type[2][1] == self.__type[2][2] == p_symbol:
                return True
            
            # check columns
            if self.__type[0][0] == self.__type[1][0] == self.__type[2][0] == p_symbol:
                return True
        
            if self.__type[0][1] == self.__type[1][1] == self.__type[2][1] == p_symbol:
                return True
            
            if self.__type[0][2] == self.__type[1][2] == self.__type[2][2] == p_symbol:
                return True
            
            # check diagonals
            if self.__type[0][0] == self.__type[1][1] == self.__type[2][2] == p_symbol:
                return True
        
            if self.__type[0][2] == self.__type[2][1] == self.__type[2][0] == p_symbol:
                return True
            
            return False
        
    def is_full(self):
        if self.__number in [1, 2]:
            for i in self.__type:
                if i == " ":
                    return False

        if self.__number in [3, 4]:
            for i in range(len(self.__type)):
                for j in range(len(self.__type[0])):
                    if self.__type[i][j] == " ":
                        return False

        return True
