def run_game():
    print("running game")


class TicTacToe:
    board = {}
    turn = 0
    winner = False
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    def player_input(self):
        for turn_number in range(1, 10):
            self.turn = turn_number
            self.print_board()
            print("Enter a position")
            selection = input()

            # while until we get a selection in the board
            while selection not in self.board or self.winner or self.board[selection] != ' ':
                print("invalid character, please try again")
                selection = input()

            else:
                self.assign_space(selection)
                print(self.board)
                if turn_number >= 5:
                    self.check_for_winner()
        if self.winner == False:
            print("it's a tie!")

    def check_for_winner(self):
        win = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'], ['7', '5', '3'], ['9', '5', '1']]
        if self.turn >= 5:
            for x in win:
                counter = 0
                for c in x:
                    if self.board[c] == 'X':
                        counter += 1
                    elif self.board[c] == 'O':
                        counter -= 1
                if counter == 3:
                    print("x wins!")
                    self.winner = True
                elif counter == -3:
                    print("o win!")
                    self.winner = True
                #debug
                #print(counter)
                #print("line check {}".format(x))

    def assign_space(self, user_input):
        if user_input in self.board and self.board[user_input] == ' ':
            if self.turn % 2 == 0:
                self.board[user_input] = 'X'
            else:
                self.board[user_input] = 'O'
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

#todo
#menu
#loop through menu. while loop = true
#one player mode
#for player 2, make random move CPU

#while loops
#accessing elements in a dict
#how to do random number
#casting variables
#vaiable scope
