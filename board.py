#from player import Player
#from board import Board

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[' ']*width for i in range(height)]
        
    def add_piece(self,piece,col):
        for row in range(self.height -1, -1, -1):
            if self.board[row][col -1] == ' ':
                self.board[row][col -1] = piece
                break
        else:
            raise ValueError('Column full')
        
                
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
        
    def check_win(self):
        c = 0
        for i in range(self.width -4):
            pass
            
            
    def is_full(self):
        for row in self.board:
            for element in row:
                if element == ' ':
                    #return False
                    print('false')
        else:
                    #return True
            print('true')
                
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
           
def main():
    bd = Board()
    bd.run()
    
if __name__ == "__main__":
    bd = Board(2,2)
    bd.add_piece('0',2)
    bd.add_piece('0',2)
    bd.add_piece(' ',1)
    bd.add_piece('x',1)
    bd.disp_board()
    bd.is_full()
    

   
        
