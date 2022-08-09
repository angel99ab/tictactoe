import os
import time
from board import Board
from player import Player


class Tictactoe:

    def __init__(self):
        self._p1 = Player("X")
        self._p2 = Player("O")
        self._board = Board()
        self._players = [self._p1, self._p2]
        self._position = 0
        self._restart = False

    def start(self):
        while True:
            try:
                self._clear_screen()
                self._show_menu()
                option = int(input("Choose an option: "))

                if option == 1:
                    self._play()
                elif option == 2:
                    pass
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

    def _show_menu(self):
        print("\n[ Tictactoe's Menu ]\n")
        print("   1) Player vs Player")
        print("   2) Player vs CPU")
        print("   3) Show matches\n")
        print("   4) Exit\n")

    def _play(self):
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
                    break

            self._position = 1 if self._position == 0 else 0

            if self._restart:
                self._position = 0
                self._restart = False

    def _clear_screen(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
            
    def _show_info(self):
        print(f"   Player {self._players[0].get_symbol()}: {self._players[0].get_wins()} wins")
        print(f"   Player {self._players[1].get_symbol()}: {self._players[1].get_wins()} wins")
        print(f"   Draws: {self._players[0].draws}\n")
        print(f"Turn of player {self._players[self._position].get_symbol()}")

    def _game_finished(self):
        p_symbol = self._players[self._position].get_symbol()
        p_wins = self._players[self._position].get_wins()
        
        if self._board.check_winner(p_symbol):
            os.system("cls")
            print("----- Player vs Player -----\n")
            self._board.display()
            print(f"Player {p_symbol} wins!")
            self._players[self._position].set_wins(p_wins + 1)
            self._board.reset()
            return True
        if self._board.is_full():
            os.system("cls")
            print(f"----- Player vs Player -----\n")
            self._board.display()
            print("It's a draw!")
            self._p1.draws += 1
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