import os
import time
from board import Board
from player import Player


class Tictactoe:

    def __init__(self):
        self._p1 = Player()
        self._p2 = Player()
        self._board = Board()
        self._players = [self._p1]
        self._position = 0
        self._correct_names = False
        self._correct_symbols = False
        self._restart = False

    def start(self):
        while True:
            try:
                self._clear_screen()
                self._show_menu("main")
                option = int(input("Choose an option: "))

                if option == 1:
                    self._play_vs("player")
                elif option == 2:
                    self._play_vs("cpu")
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

    def _show_menu(self, option):
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

    def _correct_settings(self):
        self._choose_board()
        self._choose_names()
        self._choose_symbols()

        while True:
            self._clear_screen()
            self._show_menu("player")
            input_player_p = int(input("Choose an option: "))

            if input_player_p == 1:
                return True
            elif input_player_p == 2:
                self._board.set_type(None)
                self._choose_board()
            elif input_player_p == 3:
                self._correct_names = False
                self._choose_names()
            elif input_player_p == 4:
                self._choose_symbols()
            elif input_player_p == 5:
                break
            else:
                print("No option available!")
                time.sleep(1.10)

    def _choose_board(self):
        while self._board.get_type() == None:
            self._clear_screen()
            print(f"----- Player vs Player -----\n")
            print("  [ Settings ]")
            self._board.show_types()
            option = int(input("  Choose a board: "))

            if option in [1, 2]:
                self._board.set_number(option)
                self._board.set_type([
                            " ", " ", " ",
                            " ", " ", " ",
                            " ", " ", " "
                ])
            elif option in [3, 4]:
                self._board.set_number(option)
                self._board.set_type([
                            [" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
                ])
            else:
                print("  Numbers between 1-4!")
                time.sleep(2)

    def _choose_names(self):
        while not self._correct_names:
            self._clear_screen()
            print("----- Player vs Player -----\n")
            print("  [ Settings ]\n")

            input_name1 = input("  Name of player 1: ")
            input_name2 = input("  Name of player 2: ")

            self._p1.set_name(input_name1)
            self._p2.set_name(input_name2)

            if self._p1.is_valid_name() and self._p2.is_valid_name():
                self._correct_names = True
                break
            else:
                print("  Empty names are not allowed and max characters per name is 10")
                time.sleep(2.5)
    
    def _choose_symbols(self):
        while not self._correct_symbols:
            self._clear_screen()
            print("----- Player vs Player -----\n")
            print("  [ Settings ]\n")
            print(f"  1) {self._p1.get_name()} -> X  {self._p2.get_name()} -> O")
            print(f"  2) {self._p1.get_name()} -> O  {self._p2.get_name()} -> X\n")

            input_player = int(input("Choose an option: "))

            if input_player == 1:
                self._p1.set_symbol("X")
                self._p2.set_symbol("O")
                break
            elif input_player == 2:
                self._p1.set_symbol("O")
                self._p2.set_symbol("X")
                break
            else:
                print("No option available!")
                time.sleep(1.10)

    def _play_vs(self, game_mode):
        if game_mode == "player" and self._correct_settings():
            self._players.append(self._p2)
            while True:
                self._clear_screen()
                print(f"----- Player vs Player -----\n")
                self._board.display()
                self._show_info()
                self._board.update_pos(self._players[self._position].get_symbol())

                if self._game_finished():
                    if self._play_again():
                        self._restart = True
                    else:
                        self._reset_attributes()
                        self._players.remove(self._p2)
                        break

                self._position = 1 if self._position == 0 else 0

                if self._restart:
                    self._position = 0
                    self._restart = False

    def _clear_screen(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
            
    def _show_info(self):
        print(f"   {self._players[0].get_name()}: {self._players[0].get_wins()} wins")
        print(f"   {self._players[1].get_name()}: {self._players[1].get_wins()} wins")
        print(f"   Draws: {self._players[0].draws}\n")
        print(f"Turn of {self._players[self._position].get_name()}, symbol {self._players[self._position].get_symbol()}")

    def _game_finished(self):
        p_name = self._players[self._position].get_name()
        p_symbol = self._players[self._position].get_symbol()
        p_wins = self._players[self._position].get_wins()
        
        if self._board.check_winner(p_symbol):
            os.system("cls")
            print("----- Player vs Player -----\n")
            self._board.display()
            print(f"{p_name} wins!")
            self._players[self._position].set_wins(p_wins + 1)
            self._board.reset()
            return True
        if self._board.is_full():
            os.system("cls")
            print(f"----- Player vs Player -----\n")
            self._board.display()
            print("It's a draw!")
            self._p1 += 1
            self._board.reset()
            return True

        return False

    def _play_again(self):
        play_again = "a"

        while play_again != "y" and play_again != "n":
            play_again = input("Do you want to play again [y/n]: ")

            if play_again.lower() == "y":
                return True
            elif play_again.lower() == "n":
                return False
    
    def _reset_attributes(self):
        self._p1.set_wins(0)
        self._p1.draws = 0
        self._p2.set_wins(0)
        self._board.set_type(None)
        self._correct_names = False
        self._correct_symbols = False