import random

class TicTacToe:
    board = {}
    game_type = ''

    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    def start_menu(self):
        in_progress = True
        self.winner = False
        self.turn = 0

        while in_progress:
            print("Shat would you like to do?")
            print("S = Start game")
            print("E = Exit")
            menu_selection = input()
            if menu_selection.upper() == 'S':
                print("Play against CPU or Human?")
                vs_selection = input()
                if vs_selection.upper() == "HUMAN":
                    tic_tac.game_loop("human")
                elif vs_selection.upper() == 'CPU':
                    tic_tac.game_loop("easy")
                    in_progress = False
                else:
                    print("Not a valid selection.")
            elif menu_selection.upper() == 'E':
                in_progress = False
            else:
                print("Not a valid selection.")

    def game_loop(self, game_type):
        self.game_type = game_type
        current_player = "human"

        for turn_number in range(1, 10):
            self.turn = turn_number
            if game_type == "human":
                self.print_board()
                print("Enter a position:")
                self.get_selection("human")
            else:
                if current_player == "human":
                    self.print_board()
                    print("Enter a position:")
                    self.get_selection("human")
                    current_player = game_type
                else:
                    self.get_selection(game_type)
                    current_player = "human"

        if not self.winner:
            print("It's a tie!")

    def get_selection(self, vs_mode):
        if vs_mode == "human":
            selection = input()
        elif vs_mode == "easy":
            selection = self.easy_cpu()
        while selection not in self.board or self.winner or self.board[selection] != ' ':
            if vs_mode == "human":
                print("invalid character, please try again.")
                selection = input()
            elif vs_mode == "easy":
                selection = self.easy_cpu()
        self.assign_space(selection)
        if self.turn >= 5:
            self.check_for_winner()
    def easy_cpu(self):
        return str(random.randint(1, 9))

    def hard_cpu(self):
        """
        rules for hard cpu
        read the board in current state
        if cpu can win this turn, take
        if player is going to win, take
        if middle space is not taken, take

        """

    def check_for_winner(self):
        win = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],
               ['7', '5', '3'], ['9', '5', '1']]
        if self.turn >= 5:
            for x in win:
                counter = 0
                for c in x:
                    if self.board[c] == 'X':
                        counter += 1
                    elif self.board[c] == 'O':
                        counter -= 1
                if counter == 3:
                    print("X wins!")
                    self.winner = True
                    tic_tac.clear_board()
                    tic_tac.start_menu()
                elif counter == -3:
                    print("O wins!")
                    self.winner = True
                    tic_tac.clear_board()
                    tic_tac.start_menu()

    def clear_board(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    def assign_space(self, user_input):
        if user_input in self.board and self.board[user_input] == ' ':
            if self.turn % 2 == 0:
                self.board[user_input] = 'X'
            else:
                self.board[user_input] = 'O'
        else:
            print("Invalid character.")

    def print_board(self):
        print(self.board['7'] + " | " + self.board['8'] + " | " + self.board['9'])
        print("_________")
        print(self.board['4'] + " | " + self.board['5'] + " | " + self.board['6'])
        print("_________")
        print(self.board['1'] + " | " + self.board['2'] + " | " + self.board['3'])

if __name__ == "__main__":
    tic_tac = TicTacToe()
    tic_tac.start_menu()

# todo
# menu
# loop through menu. while loop = true
# one player mode
# for player 2, make random move CPU

# while loops
# accessing elements in a dict
# how to do random number
# casting variables
# vaiable scope


# QEUSTIONS
# clean up code by using .upper on strings? cpu, menu selection
