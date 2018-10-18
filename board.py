#from player import Player
#from board import Board

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[' ']*width for i in range(height)]
        
    def add_piece(self,col,piece):
        if col > self.width or col < 1 :
            raise ValueError('Invalid Column')
        for row in range(self.height -1, -1, -1):
            if self.board[row][col -1] == ' ':
                self.board[row][col -1] = piece
                break
        else:
            raise ValueError('Column Full')
                
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
        
    def check_win(self):
        #check horiz win
        for row in range(self.height):
            for c in range(self.width -3):
                if (self.board[row][c] == self.board[row][c+1] == self.board[row][c+2] == self.board[row][c+3] != ' '):
                    #print('win')
                    return True  

        #check vert win
        for row in range(self.height -3):
            for c in range(self.width):
                if (self.board[row][c] == self.board[row+1][c] == self.board[row+2][c] == self.board[row+3][c] != ' '):
                    #print('win')
                    return True
                
        #check / win
        for row in range(3,self.height):
            for c in range(self.width -3):
                if (self.board[row][c] == self.board[row-1][c+1] == self.board[row-2][c+2] == self.board[row-3][c+3] != ' '):
                    return True
                 
        #check \ win
        for row in range(self.height -3):
            for c in range(self.width -3):
                if (self.board[row][c] == self.board[row+1][c+1] == self.board[row+2][c+2] == self.board[row+3][c+3] != ' '):
                    return True

        return False
                   
    def is_full(self):             
        for row in self.board:
            for element in row:                
                if element == ' ':
                    #print('false')
                    return False              
        return True
                
    def disp_board(self):
                
        for i in range(self.width*2):
            print('-',end='')           
        print()
        for row in self.board:
            for element in row:
                print(element,end=' ')
            print() 
        for i in range(self.width*2):
            print('-',end='')           
        print()
        for i in range(self.width):
            print(i + 1,end=' ')

#        for row in self.board:
#            for element in row:
#                print(element,end=' ')
#            print()
#        for i in range(self.width):
#            print(i + 1,end=' ')
           
def main():
    bd = Board()
    bd.run()
    
if __name__ == "__main__":
    main()
