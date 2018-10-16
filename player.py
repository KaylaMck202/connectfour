from board import Board
class Player:
    def __init__(self,piece):
        self.name = self.get_name
        self.piece = piece
        self.choice = self.get_choice
    def get_name(self):
        self.name = input("What is your name?")
#        p1 = player1
#        p2
    def get_choice(self,board):
        choice = int(input(f"{player[turn].name} pick column"))
        return choice 
        #pass
    
if __name__=="__main__":
    Player(2)
    #pass