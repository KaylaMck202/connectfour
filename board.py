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
        num_inrow = 0
        for row in range(self.height):
            for col in range(self.width -4):
                if self.board[row][col] == 'x':
                    num_inrow += 1
                if not self.board[row][col] == 'x':
                    num_inrow = 0
                if num_inrow >= 4:
                    print('true')  #get rid of in final
                    return True
                
        num_inrow = 0
        for row in range(self.height):
            for c in range(self.width -4):
                if self.board[row][col] == 'o':
                    num_inrow += 1
                if not self.board[row][col] == 'o':
                    num_inrow = 0
                if c >= 4:
                    print('true')  #get rid of in final
                    return True

                
                     
    def is_full(self):             
        for row in self.board:
            for element in row:                
                if element == ' ':
                    #print('false')
                    return False
                    
        else:
            #print('true')
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
           
def main():
    bd = Board()
    bd.run()
    
if __name__ == "__main__":
    bd = Board(6,7)
    bd.add_piece('x',4)
    bd.add_piece('x',5)
    bd.add_piece('x',1)
    bd.add_piece('x',2)
    bd.add_piece('x',3)
    bd.add_piece('i',3)
    bd.disp_board()
    bd.check_win()

