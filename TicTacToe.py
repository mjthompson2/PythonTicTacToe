def run_game():
    print("running game")


class TicTacToe:
    board = {}
    turn = 0

    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    # todo add check for victory

    def player_input(self):
        for turn_number in range(1, 10):
            self.turn = turn_number
            self.print_board()
            print("Enter a position")
            selection = input()
            # while until we get a selection in the board
            while selection not in self.board:
                print("invalid character, please try again")
                selection = input()
            else:
                self.assign_space(selection)

    def assign_space(self, user_input):
        if user_input in self.board and self.board[user_input] == ' ':
            if self.turn % 2 == 0:
                self.board[user_input] = "X"
            else:
                self.board[user_input] = "0"
        else:
            print("invalid character")

    def print_board(self):
        print(self.board['7'] + " | " + self.board['8'] + " | " + self.board['9'])
        print("_________")
        print(self.board['4'] + " | " + self.board['5'] + " | " + self.board['6'])
        print("_________")
        print(self.board['1'] + " | " + self.board['2'] + " | " + self.board['3'])


if __name__ == "__main__":
    tic_tac = TicTacToe()
    tic_tac.player_input()
