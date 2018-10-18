from board import Board
class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
    def get_name(self):
        self.name = input("What is your name?")
        return self.name

    def get_choice(self):
        choice = int(input(f"{self.name} pick column"))
        return int(choice) 
        #pass
    
if __name__=="__main__":
    Player('o')
    #pass