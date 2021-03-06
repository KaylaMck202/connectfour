from board import Board
from player import Player

class Game:
    def __init__(self):
        '''greets the players, asks for the player's name,
            creates the board, and starts the game.'''
        
        print("Hello and welcome to Connect Four!")
        self.players = []
        self.players.append(Player('x'))
        self.players.append(Player('o'))
        self.board = Board(7,6) 
        self.turn = 0
        self.game = self.play_game()
        
        
        #pass
    def play_game(self):
        '''displays the board, asks the player what column
            they would like their piece to be placed, checks
            for win and prints who won.It also checks if the board
            is full, if so it prints out "it's a draw". The turn
            changes.'''
    
        while True:
            try:
                self.board.disp_board()
                self.choice = self.players[self.turn].get_choice()
                self.board.add_piece(self.choice, self.players[self.turn].piece)
                self.board.check_win()
                if self.board.check_win()==True:
                    self.board.disp_board()
                    print()
                    print(f"{self.players[self.turn].name} wins!")
                    #return
                    break
#                if self.board.check_win()==False:
#                    self.board.disp_board()
                if self.board.is_full() == True:
                    self.board.disp_board()
                    print()
                    print("it's a draw")
                    return
                self.turn =(self.turn+1)%2
            except Exception as e:
                print()
                print(f'That was not valid! {str(e)}')
        
if __name__=="__main__":
    #pass
    #Player()
    #test code
    Game()
    