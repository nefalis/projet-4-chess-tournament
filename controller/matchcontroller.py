"""
Fonction a faire
- ajout point 
- debut match
- fin match
- melange joueur aleatoire
- association de joueur
- verif si match identique

"""

from models.match import Match
from models.player import Player

class MatchController:
    def add_match(self, player1, player2, first_name, last_name, color_player1, color_player2):
        player1 = first_name + last_name + color_player1
        player2 = first_name + last_name + color_player2
        if player1 and player2:
            match = Match(player1, player2)
            self.add_match(match)
        else:
            print("Erreur: JOUEUR non trouvé")
