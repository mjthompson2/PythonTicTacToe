def run_game():
    print("running game")


class TicTacToe:
    board = {}
    turn = 0

    def __init__(self):
        self.board = {7: ' ', 8: ' ', 9: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      1: ' ', 2: ' ', 3: ' '}

    def player_input(self):
        for turn_number in range(1, 10):
            self.turn = self.turn + 1
            self.print_board()
            print("Enter a position")
            selection = input()
            self.assign_space(selection)

    def assign_space(self, input):
        if input in self.board and self.board[input] == ' ':
            if self.turn % 2 == 0:
                self.board[input] = "X"
            else:
                self.board[input] = "0"

    def print_board(self):
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])
        print("_________")
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
        print("_________")
        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])


##    def check_for_winner():

##  def assign_square():


if __name__ == "__main__":
    tic_tac = TicTacToe()
    tic_tac.player_input()
