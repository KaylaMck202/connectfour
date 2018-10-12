from player import Player
#from board import Board

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[' ']*width for i in range(height)]
        
    def add_piece(self,piece,col):
        
                
    def empty_board(self):
        self.board = [[' ']*width for i in range(height)]
        print(self.board)
    def check_win(self):
        if len(height):
            pass
    def is_full(self):
        if numpieces == (self.width * self.height):
            True
        else:
            False
    def disp_board(self):
        print(self.board)
        
#def main():
#    bd = Board()
#    bd.run()
    
if __name__ == "__main__":
    #test code
    pass
        