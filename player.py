#from board import Board
class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
    def get_name(self):
        name1 = input("Insert Player 1 name: ")
        name2 = input("Insert Player 2 name: ")
        self.get_choice()
        #pass
    
    def get_choice(self,board):
        choice = int(input("What column do you want to place your chip?:"))
        col = choice
            
        #pass
    
    
    
if __name__=="__main__":
    #test code
    #Player()
    pass