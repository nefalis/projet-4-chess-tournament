from controller.tournamentcontroller import TournamentController
from datetime import datetime

class RoundView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller


    """ fonction pour commencer un tournoi """
    def display_menu_tournament():
        print("Commencer un tournoi")
        print("1 Commencer le tournoi")
        print("2 Commencer le 1er round")
        print("3 Commencer le 2eme round")
        print("4 Commencer le 3eme round")
        print("5 Commencer le 4eme round")
        print("6 Fin du tournoi")
        print("7 Quitter le menu du tournoi en cours")

    def start_tournament(self):
        start_time = datetime.now()
        # pour mettre a jour la date et heure au début du tournoi
        if self.tournament_controller.current_tournament:
            self.tournament_controller.current_tournament.start_time = start_time
        
        print(f"Le tournoi démarre à : {start_time}")

    def start_first_round(self):
        # verifier si il y a un tournoi en cours
        if self.tournament_controller.current_tournament is None:
            print("Aucun tournoi en cours.")
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
        print("Le premier round du tournoi a démarré avec succès.")