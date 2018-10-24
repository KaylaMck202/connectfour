from board import Board
class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
    def get_name(self):
        '''asks for the player's name and stores it'''
        self.name = input("What is your name?")
        return self.name # unnecessary

    def get_choice(self):
        '''asks the player what column they want to place
            their piece and stores it.'''
        choice = int(input(f"{self.name} pick column:"))
        return int(choice) 
        #pass
    
if __name__=="__main__":
    Player('o')
    #pass