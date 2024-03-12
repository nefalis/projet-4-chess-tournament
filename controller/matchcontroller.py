
from models.match import Match

class MatchController:

    def __init__(self):
        self.matches = []

    def add_match(self, player1, player2, color_player1, color_player2):
        match = Match(player1, player2, color_player1, color_player2)
        self.matches.append(match)
        return match

    def end_match(self, match, winner):
        match.winner = winner
        # Mettre à jour les joueurs avec le résultat du match
        if winner:
            # Incrémente le score du joueur gagnant
            winner.score += 1  
            # Déterminez le perdant et mettez à jour son score à 0
            loser = match.player1 if winner != match.player1 else match.player2
            loser.score = 0
        else:
            # Si le match se termine par une égalité, ajoutez 0.5 à chaque joueur
            for player in [match.player1, match.player2]:
                player.score += 0.5

