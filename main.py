class TicTacToe:
    def __init__(self):
        self.player_1 = str()
        self.player_2 = str()
        self.names = list()
        self.t_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.after_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def show_board(self, xo_plot):
        print('| ' + xo_plot[7]+ ' | ' + xo_plot[8] +  ' | ' + xo_plot[9] + ' |' )
        print('---------------')
        print('| ' + xo_plot[6]+ ' | ' + xo_plot[5] +  ' | ' + xo_plot[4] + ' |' )
        print('---------------')
        print('| ' + xo_plot[1]+ ' | ' + xo_plot[2] +  ' | ' + xo_plot[3] + ' |' )

    def rules(self):
        print("1. The game is played on a grid that's 3 squares by 3 squares.\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
        print("For more info : You can Visit : https://en.wikipedia.org/wiki/Tic-tac-toe")

    def opening_screen(self):
        print('-----------------------')
        print('TicTacToe - Saugat Khanal')
        print('-----------------------')
        self.player_1 = input('First Player (O) : ')
        self.player_2 = input('Second Player (X) : ')
        print(f'{self.player_1.title()} will go first!')
        print("Do you want the rules? : ")
        rules = input("(Y) OR (N) : ")
        if rules.lower() == 'y':
            self.rules()
        elif rules.lower() == 'n':
            print("Good Luck!")
            self.plot()

    def win_check_1(self):
        if (self.after_board[1] == 'O' and self.after_board[2] == 'O' and self.after_board[3] == 'O' or
        self.after_board[4] == 'O' and self.after_board[5] == 'O' and self.after_board[6] == 'O' or
        self.after_board[7] == 'O' and self.after_board[8] == 'O' and self.after_board[9] == 'O' or
        self.after_board[1] == 'O' and self.after_board[6] == 'O' and self.after_board[7] == 'O' or
        self.after_board[2] == 'O' and self.after_board[5] == 'O' and self.after_board[8] == 'O' or
        self.after_board[3] == 'O' and self.after_board[4] == 'O' and self.after_board[9] == 'O' or
        self.after_board[1] == 'O' and self.after_board[5] == 'O' and self.after_board[9] == 'O' or
        self.after_board[7] == 'O' and self.after_board[5] == 'O' and self.after_board[3] == 'O'):
            print(f"{self.player_1.title()} is the winner!")
            play_again1 = input("Do you want to play again? : (Y/N) : ")
            if play_again1.lower() == 'y':
                self.after_board = [' '] * 10
                self.run_game()
            else:
                quit()

    def win_check_2(self):
        if (self.after_board[1] == 'X' and self.after_board[2] == 'X' and self.after_board[3] == 'X' or
        self.after_board[4] == 'X' and self.after_board[5] == 'X' and self.after_board[6] == 'X' or
        self.after_board[7] == 'X' and self.after_board[8] == 'X' and self.after_board[9] == 'X' or
        self.after_board[1] == 'X' and self.after_board[6] == 'X' and self.after_board[7] == 'X' or
        self.after_board[2] == 'X' and self.after_board[5] == 'X' and self.after_board[8] == 'X' or
        self.after_board[3] == 'X' and self.after_board[4] == 'X' and self.after_board[9] == 'X' or
        self.after_board[1] == 'X' and self.after_board[5] == 'X' and self.after_board[9] == 'X' or
        self.after_board[7] == 'X' and self.after_board[5] == 'X' and self.after_board[3] == 'X'):
            print(f"{self.player_2.title()} is the winner!")
            play_again2 = input("Do you want to play again? : (Y/N) ")
            if play_again2.lower() == 'y':
                self.after_board = [' '] * 10
                self.run_game()
            else:
                quit()
    
    def plot(self):
        while True:
            p1_input = int(input(f"{self.player_1.title()} : (O) "))
            self.after_board[p1_input] = 'O'
            self.show_board(self.after_board)
            self.win_check_1()
            p2_input = int(input(f"{self.player_2.title()} : (X) "))
            self.after_board[p2_input] = 'X'
            self.show_board(self.after_board)
            self.win_check_2()




    def run_game(self):
        self.show_board(self.t_board)
        self.opening_screen()
        self.plot()


#THIS IS AN ADDED TEXT TOOOOOOOOOOOOOOO

#ADDED TEXTT WOOOOOOOOOOOO

if __name__ == '__main__':
    game = TicTacToe()
    game.run_game()



