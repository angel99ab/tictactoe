import os
import time
from board import Board
from player import Player


class Tictactoe:

    def __init__(self):
        self._players = [Player("X"), Player("O")]
        self._board = Board()

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
        position = 0

        while True:
            self._clear_screen()
            print(f"----- Player vs Player -----\n")
            self._board.display()
            self._show_info(position)
            self._board.update_pos(self._players[position].get_symbol())

            if self._game_finished(position):
                if self._play_again():
                    position = 0
                else:
                    self._reset_attributes()
                    break

            position = 1 if position == 0 else 0

    def _clear_screen(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
            
    def _show_info(self, player_position):
        print(f"   Player {self._players[0].get_symbol()}: {self._players[0].get_wins()} wins")
        print(f"   Player {self._players[1].get_symbol()}: {self._players[1].get_wins()} wins")
        print(f"   Draws: {self._players[0].draws}\n")
        print(f"Turn of player {self._players[player_position].get_symbol()}")

    def _game_finished(self, player_position):
        p_symbol = self._players[player_position].get_symbol()
        p_wins = self._players[player_position].get_wins()
        
        if self._board.check_winner(p_symbol):
            os.system("cls")
            print("----- Player vs Player -----\n")
            self._board.display()
            print(f"Player {p_symbol} wins!")
            self._players[player_position].set_wins(p_wins + 1)
            self._board.reset()
            return True
        if self._board.is_full():
            os.system("cls")
            print(f"----- Player vs Player -----\n")
            self._board.display()
            print("It's a draw!")
            self._players[0].draws += 1
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
        for player in self._players:
            player.set_wins(0)

        self._players[0].draws = 0
        