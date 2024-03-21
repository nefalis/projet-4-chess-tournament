
from models.round import Match

class RoundController:

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

    """ fonction pour enregistrer les résultat du 1er round """
    def record_match_results(self, round_number):
        print(f"Enregistrement des résultats du round {round_number} :")
        for match in self.round_controller.matches[:4]:
            print(f"Match : {match.player1.name} vs {match.player2.name}")
            while True:
                winner = input("Vainqueur (entrez le nom du vainqueur, 'egalite' pour un match nul, ou 'back' pour revenir en arrière) : ")
                if winner.lower() == 'egalite':
                    match.end_match(None)
                    break
                # pour revenir en arrire
                elif winner.lower() == 'back':
                    break 
                elif winner.strip():  
                    if winner == match.player1.name:
                        match.end_match(match.player1)
                        break
                    elif winner == match.player2.name:
                        match.end_match(match.player2)
                        break
                    else:
                        print("Nom de joueur invalide. Veuillez réessayer")
                else:
                    print("Veuillez saisir un nom de joueur ou 'egalite' pour un match nul, ou 'back' pour revenir en arrière")

        print("Les résultats du premier round ont été enregistrés avec succès")