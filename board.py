from player import Player
#from board import Board

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def place_piece(self,piece,col):
        pass
    def empty_board(self):
        pass
    def check_win(self):
        pass
    def is_full(self):
        pass
    def disp_board(self):
        board = [[' ']*width for i in range(height)]
        print(board)
    
if __name__ == "__main__":
    #test code
    pass
        