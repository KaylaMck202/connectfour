#from player import Player
#from board import Board

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[' ']*width for i in range(height)]
        
    def add_piece(self,piece,col):
        pass
        
                
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
        
    def check_win(self):
        if len(height):
            pass
    def is_full(self):
        for row in self.board:
            for element in row:
                if element == ' ':
                    return False
                else:
                    return True
                
    def disp_board(self):
        for row in self.board:
            for element in row:
                print(element,end=' ')
            print()
            
        for i in range(self.width):
            print('_',end=' ')
            
        print()            
        for i in range(self.width):
            print(i + 1,end=' ')
           
#def main():
#    bd = Board()
#    bd.run()
    
if __name__ == "__main__":
    bd = Board(8,8)
    bd.disp_board()
    
#for i in range(self.height-1, 0, -1):            
#            if self.board[i][column-1] != ' ':
#                self.board[i][column-1] = piece
#                break 
   
        
