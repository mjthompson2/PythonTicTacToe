def run_game():
    print("running game")


class TicTacToe:
    board = {}
    turn = 0
    p1 = {'7': ' ', '8': ' ', '9': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '1': ' ', '2': ' ', '3': ' '}
    p2 = {'7': ' ', '8': ' ', '9': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '1': ' ', '2': ' ', '3': ' '}

    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    if turn >= 5:
        if board

    # todo add check for victory
    # This is too hard for me right now.
    # def victory_screen(self):
    #     win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    #     for x in win:
    #         if sum(x) == 15:
    #             print("p1 wins")
    #         elif sum(x) == -15:
    #             print("p2 wins")
    #         else:
    #             print("tie")
    #     """
    #      2 7 6
    #      9 5 1
    #      4 3 8
    #     """
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
