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
            raise ValueError('Column Full')
                
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
        
    def check_win(self):       
        for row in range(self.height):
            for c in range(self.width -4):
                if (self.board[row][c] == self.board[row][c+1] == self.board[row][c+2] == self.board[row][c+3] != ' '):
                    #print('win')
                    return True  
#                else:
#                    print('not win')
#                    return False

        for row in range(self.height):
            for col in range(self.width):
                pass
                            
                   
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
#        for row in self.board:
#            for element in row:
#                print(element,end=' ')
#            print()           
#        for i in range(self.width):
#            print('_',end=' ')           
#        print()            
#        for i in range(self.width):
#            print(i + 1,end=' ')

        for row in self.board:
            for element in row:
                print(element,end=' ')
            print()
        for i in range(self.width):
            print(i + 1,end=' ')
           
def main():
    bd = Board()
    bd.run()
    
if __name__ == "__main__":
    bd = Board(7,6)
#    bd.add_piece(' ',4)
#    bd.add_piece(' ',5)
#    bd.add_piece(' ',1)
#    bd.add_piece(' ',2)
#    bd.add_piece(' ',3)
#    bd.add_piece(' ',3)
#    bd.add_piece(' ',6)
    bd.disp_board()
#    bd.check_win()

