import random

class TicTacToe:
    board = {}
    turn = 0
    winner = False

    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    # #select random player
    #
    # def first_player():
    #     if random.randint(0, 1) == 0:
    #         return 'computer'
    #     else:
    #         return 'player'
    #
    # #computer movement
    # # choose number between 1-9. if selection in self.board is free, choose space, if not, choose another.
    def assign_space(self, user_input):
        if user_input in self.board and self.board[user_input] == ' ':
            if self.turn % 2 == 0:
                self.board[user_input] = 'X'
            else:
                self.board[user_input] = 'O'
        else:
            print("Invalid character.")

    def simple_cpu(self):
        selection = random.randint(1,9)
        print(selection)
        while selection not in self.board or self.winner or self.board[selection] != ' ':
            self.assign_space(selection)
            print(self.board)



if __name__ == "__main__":
    tic_tac = TicTacToe()
        #tic_tac.start_menu()

