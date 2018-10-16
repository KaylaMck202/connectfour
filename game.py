from board import Board
from player import Player

class Game:
    def __init__(self):
        turn = 0
        self.players = []
#        self.players.append(Player())
#        self.players.append(Player())
        self.board = Board(7,6) 
        #pass
    def play_game(self):
        board.add_piece()
        if board.check_win():
            print(f"{players[turn]} wins")
            return
        if board.is_full():
            print("it's a draw")
            return
        turn =(turn+1)%2
        
        #self.width = input("What width do you want your board to be? ")
        #pass
#def main:
#    pass
if __name__=="__main__":
    #pass
    #Player()
    #test code
    Game()
    