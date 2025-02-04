""" Write a `Game` class that keeps track of player scores. 
    Use a private dictionary to store player names and their scores. 
    Add methods to update scores and display rankings in descending order.
"""

class Game:
    def __init__(self):
        self.game={}

    def add_player(self,name):
        if name not in self.game:
            self.game[name]=0
        else:
            print("player",name,"is already in the dictionary")

    def update_score(self, name, score):
        if name in self.game:
            self.game[name]+=score
        else:
            print("player",name,"not existed in the dictionary, please add the player into dictionary")

    def display_score_ranking(self):
        sorted_scores = sorted(self.game.items(), key=lambda x: x[1], reverse=True)
        
        print("Rankings:")
        idx = 1
        for player, score in sorted_scores:
            print(idx, ".", player, "-", score, "runs")
            idx += 1 

game = Game()
game.add_player("virat")
game.add_player("rohit")
game.update_score("virat", 103)
game.update_score("rohit", 92)
game.update_score("virat", 183)
game.display_score_ranking()