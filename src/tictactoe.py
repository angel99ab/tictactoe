import os
import time
from board import Board
from player import Player
from cpu import Cpu


class Tictactoe:

    def __init__(self):
        self.__p1 = Player()
        self.__p2 = Player()
        self.__cpu = Cpu()
        self.__board = Board()
        self.__players = [self.__p1]
        self.__position = 0
        self.__correct_names = False
        self.__correct_symbols = False
        self.__restart = False

    def start(self):
        while True:
            try:
                self.__clear_screen()
                self.__show_menu("main")
                option = int(input("Choose an option: "))

                if option == 1:
                    self.__play_vs("player")
                elif option == 2:
                    self.__play_vs("cpu")
                elif option == 3:
                    pass
                elif option == 4:
                    break
                else:
                    print("Numbers between 1-4!")
                    time.sleep(1.5)
            except ValueError:
                print("Only numbers are allowed!")
                time.sleep(1.5)

    def __show_menu(self, option):
        if option == "main":
            print("\n[ Tictactoe's Menu ]\n")
            print("   1) Player vs Player")
            print("   2) Player vs CPU")
            print("   3) Show matches\n")
            print("   4) Exit\n")
        elif option == "player":
            print("----- Player vs Player -----\n")
            print("  [ Settings ]\n")
            print("  1) Start match")
            print("  2) Change board")
            print("  3) Change names")
            print("  4) Change players symbols\n")
            print("  5) Go to main menu\n")

    def __correct_settings(self):
        self.__choose_board()
        self.__choose_names()
        self.__choose_symbols()

        while True:
            self.__clear_screen()
            self.__show_menu("player")
            input_player_p = int(input("Choose an option: "))

            if input_player_p == 1:
                return True
            elif input_player_p == 2:
                self.__board.set_type(None)
                self.__choose_board()
            elif input_player_p == 3:
                self.__correct_names = False
                self.__choose_names()
            elif input_player_p == 4:
                self.__choose_symbols()
            elif input_player_p == 5:
                break
            else:
                print("No option available!")
                time.sleep(1.10)

    def __choose_board(self):
        while self.__board.get_type() == None:
            self.__clear_screen()
            print(f"----- Player vs Player -----\n")
            print("  [ Settings ]")
            self.__board.show_types()
            option = int(input("  Choose a board: "))

            if option in [1, 2]:
                self.__board.set_number(option)
                self.__board.set_type([
                            " ", " ", " ",
                            " ", " ", " ",
                            " ", " ", " "
                ])
            elif option in [3, 4]:
                self.__board.set_number(option)
                self.__board.set_type([
                            [" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
                ])
            else:
                print("  Numbers between 1-4!")
                time.sleep(2)

    def __choose_names(self):
        while not self.__correct_names:
            self.__clear_screen()
            print("----- Player vs Player -----\n")
            print("  [ Settings ]\n")

            input_name1 = input("  Name of player 1: ")
            input_name2 = input("  Name of player 2: ")

            self.__p1.set_name(input_name1)
            self.__p2.set_name(input_name2)

            if self.__p1.is_valid_name() and self.__p2.is_valid_name():
                self.__correct_names = True
                break
            else:
                print("  Empty names are not allowed and max characters per name is 10")
                time.sleep(2.5)
    
    def __choose_symbols(self):
        while not self.__correct_symbols:
            self.__clear_screen()
            print("----- Player vs Player -----\n")
            print("  [ Settings ]\n")
            print(f"  1) {self.__p1.get_name()} -> X  {self.__p2.get_name()} -> O")
            print(f"  2) {self.__p1.get_name()} -> O  {self.__p2.get_name()} -> X\n")

            input_player = int(input("Choose an option: "))

            if input_player == 1:
                self.__p1.set_symbol("X")
                self.__p2.set_symbol("O")
                break
            elif input_player == 2:
                self.__p1.set_symbol("O")
                self.__p2.set_symbol("X")
                break
            else:
                print("No option available!")
                time.sleep(1.10)

    def __play_vs(self, game_mode):
        if game_mode == "player" and self.__correct_settings():
            self.__players.append(self.__p2)
            while True:
                self.__clear_screen()
                print(f"----- Player vs Player -----\n")
                self.__board.display()
                self.__show_info()
                self.__board.update_pos(self.__players[self.__position].get_symbol())

                if self.__game_finished():
                    if self.__play_again():
                        self.__restart = True
                    else:
                        self.__reset_attributes()
                        self.__players.remove(self.__p2)
                        break

                self.__position = 1 if self.__position == 0 else 0

                if self.__restart:
                    self.__position = 0
                    self.__restart = False
        elif game_mode == "cpu":
            pass

    def __clear_screen(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
            
    def __show_info(self):
        print(f"   {self.__players[0].get_name()}: {self.__players[0].get_wins()} wins")
        print(f"   {self.__players[1].get_name()}: {self.__players[1].get_wins()} wins")
        print(f"   Draws: {self.__players[0].draws}\n")
        print(f"Turn of {self.__players[self.__position].get_name()}, symbol {self.__players[self.__position].get_symbol()}")

    def __game_finished(self):
        p_name = self.__players[self.__position].get_name()
        p_symbol = self.__players[self.__position].get_symbol()
        p_wins = self.__players[self.__position].get_wins()
        
        if self.__board.check_winner(p_symbol):
            os.system("cls")
            print("----- Player vs Player -----\n")
            self.__board.display()
            print(f"{p_name} wins!")
            self.__players[self.__position].set_wins(p_wins + 1)
            self.__board.reset()
            return True
        if self.__board.is_full():
            os.system("cls")
            print(f"----- Player vs Player -----\n")
            self.__board.display()
            print("It's a draw!")
            self.__p1 += 1
            self.__board.reset()
            return True

        return False

    def __play_again(self):
        play_again = "a"

        while play_again != "y" and play_again != "n":
            play_again = input("Do you want to play again [y/n]: ")

            if play_again.lower() == "y":
                return True
            elif play_again.lower() == "n":
                return False
    
    def __reset_attributes(self):
        self.__p1.set_wins(0)
        self.__p1.draws = 0
        self.__p2.set_wins(0)
        self.__board.set_type(None)
        self.__correct_names = False
        self.__correct_symbols = False