from controller.tournamentcontroller import TournamentController
from controller.roundcontroller import RoundController
from datetime import datetime

class RoundView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller
        self.round_controller = RoundController()

    """ fonction pour commencer un tournoi """
    def display_menu_tournament():
        print("Commencer un tournoi")
        print("1 Commencer le tournoi")
        print("2 Commencer le 1er round")
        print("3 Passer au round suivant")
        print("4 Fin du tournoi")
        print("5 Quitter le menu du tournoi en cours")

    """ fonction pour demarrer le tournoi """
    def start_tournament_round(self):
        if self.tournament_controller.current_tournament is None:
            print("Aucun tournoi en cours.")
            return
    
        start_time = datetime.now()
        # pour mettre a jour la date et heure au début du tournoi
        self.tournament_controller.current_tournament.start_time = start_time
        print(f"Le tournoi démarre à : {start_time}")

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
            match = self.tournament_controller.match_controller.add_match(round_players[i], round_players[i + 1], "white", "black")
            match.start_match()
        print("Le premier round du tournoi a démarré avec succès")

    """ fonction pour enregistrer les résultat du 1er round """
    def record_first_round_results(self):
        print("Enregistrement des résultats pour le premier round :")
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

    """ fonction pour passer au round suivant """
    def next_round(self):
        if self.check_round_completion():
            self.tournament_controller.start_round()
        else:
            print("Les matchs du round en cours n'ont pas encore été joués")

    """ fonction pour verifier si tous les matchs du round ont été joué """
    def check_round_completion(self):
        if len(self.round_controller.matches) == 4:
            for match in self.round_controller.matches:
                if match.winner is None:
                    return False
            return True
        return False
    
