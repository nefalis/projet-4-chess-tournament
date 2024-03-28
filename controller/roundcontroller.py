from models.round import Match
from view.tournamentview import TournamentView
from datetime import datetime

class RoundController:

    def __init__(self, tournament_controller):
        self.matches = []
        self.tournament_controller = tournament_controller

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
        for match in self.matches[:4]:
            print(f"Match : {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}")
            while True:
                winner = input("Vainqueur (entrez le nom du vainqueur, 'egalite' pour un match nul, ou 'back' pour revenir en arrière) : ")
                if winner.lower() == 'egalite':
                    match.end_match(None)
                    break
                # pour revenir en arrire
                elif winner.lower() == 'back':
                    break 
                elif winner.strip():  
                    if winner == match.player1.first_name:
                        match.end_match(match.player1)
                        break
                    elif winner == match.player2.first_name:
                        match.end_match(match.player2)
                        break
                    else:
                        print("Nom de joueur invalide. Veuillez réessayer")
                else:
                    print("Veuillez saisir un nom de joueur ou 'egalite' pour un match nul, ou 'back' pour revenir en arrière")

        print("Les résultats du premier round ont été enregistrés avec succès")


    """ fonction pour demarrer le tournoi """
    def start_tournament_round(self):
    
        tournament = TournamentView.select_tournament(self.tournament_controller)
        print(f"Vous allez commencer le tournoi {tournament.name_tournament}")
        if tournament is None:
            print("Aucun tournoi sélectionné")
            return
        start_time = datetime.now()
        tournament.start_time = start_time
        print(f"Le tournoi {tournament.name_tournament} démarre à: {start_time}")
        self.tournament_controller.current_tournament = tournament
        self.tournament_controller.start_round()

    """ fonction pour demarrer le 1er round """
    def start_first_round(self):
        # verifier si il y a un tournoi en cours
        if self.tournament_controller.current_tournament is None:
            print("Aucun tournoi en cours")
            return
        # verifier si il y a assez de joueur
        if len(self.tournament_controller.current_tournament.players) < 8:
            print("Pas assez de joueurs pour démarrer le premier round.")
            return
        # Générer les matchs pour le premier round
        round_players = self.tournament_controller.current_tournament.players[:8]
        for i in range(0, len(round_players), 2):
            match = self.tournament_controller.add_match(round_players[i], round_players[i + 1], "white", "black")
            match.start_match()
        print("Le premier round du tournoi a démarré avec succès")

    """ fonction pour passer au round suivant """
    def next_round(self):
        if self.check_round_completion():
            self.tournament_controller.start_round()
        else:
            print("Les matchs du round en cours n'ont pas encore été joués")

    """ fonction pour verifier si tous les matchs du round ont été joué """
    def check_round_completion(self):
        if len(self.matches) == 4:
            for match in self.matches:
                if match.winner is None:
                    return False
            return True
        return False
    
    """ fonction pour creer les matchs pour 1 round  """
    def create_matches(self, round_players):
        matches =[]
        for i in range(0, len(round_players), 2):
            match = self.match_controller.add_match(round_players[i], round_players[i + 1], "white", "black")
            matches.append(match)
        return matches
    
    """ fonction pour afficher les joueurs des matchs"""
    def display_matches(self, matches):
        for e, match in enumerate(matches, start=1):
            print(f"Match {e}: {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}")