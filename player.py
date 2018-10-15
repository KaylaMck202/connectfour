#from board import Board
class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        #self.choice = self.get_choice()
    def get_name(self):
        self.name = input("What is your name?")
    
    def get_choice(self,board):
        #choice = int(input("What column do you want to place your chip?:"))
        pass
    
def main():   
    pass
if __name__=="__main__":
    #test code
    Player(2)
    #pass