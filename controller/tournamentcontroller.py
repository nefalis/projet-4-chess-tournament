
import json
import os

from controller.playercontroller import PlayerController
from controller.matchcontroller import MatchController
from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.match_controller = MatchController()
        self.tournament_model = Tournament
        self.current_tournament = None
        self.tournaments = []

    """ fonction pour creer un tournois"""
    def create_tournament(self, name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament):
        new_tournament = self.tournament_model(name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament)
        self.current_tournament = new_tournament  # Assigner le nouveau tournoi à la variable current_tournament
        self.tournaments.append(new_tournament)  # Ajoutez le nouveau tournoi à la liste
        print("nouveau tournoi")
        print(self.tournaments)
        return new_tournament
    
    """ fonction pour creer un fichier json"""
    def create_tournament_json(self, filename):
        data_folder = "data"
        full_path = os.path.join(data_folder, filename)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        if not os.path.exists(full_path):
            with open(full_path, 'w') as f:
                json.dump([], f)  # Crée un fichier JSON vide
        with open(full_path, 'r') as f:
            tournaments_data = json.load(f)
            self.tournaments = [Tournament(**tournament_data) for tournament_data in tournaments_data]
            
    """ fonction pour mettre a jour le fichier json """
    def update_tournament_json(self, filename):
        data_folder = "data"
        full_path = os.path.join(data_folder, filename)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        # Récupérez les données du tournoi
        tournaments_data = [tournament.__dict__ for tournament in self.tournaments]
        # Écrivez les données dans le fichier JSON
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump(tournaments_data, json_file, indent=4, ensure_ascii=False)
    
    """ fonction pour ajouter des joueurs au tournois"""
    def add_player_tournament(self, players):
        if self.current_tournament is None:
            print("Aucun tournoi en cours")
            return
        for player in players:
            self.current_tournament.add_player(player)

    """ fonction pour commencer un tournois"""
    def start_tournament(self):
        print("start tournoi")
        for round_number in range(1, 5):
            print(f"Round {round_number}")
            self.start_round()

    """ fonction pour démarrer un tournois"""
    def start_round(self):
        # Choisissez 4 joueurs aléatoires pour le round
        round_players = self.player_controller.choose_random_players(4)
        # Créez 4 matchs avec les joueurs choisis
        for i in range(0, len(round_players), 2):
            match = self.match_controller.add_match(round_players[i], round_players[i + 1], "white", "black")
            match.start_match()
            print("start match tounoi")
            # Supposons que le premier joueur gagne
            self.match_controller.end_match(match, match.player1)

    """ fonction pour les resultats des matchs """
    def get_match_result(self):
        match_results = []
        for match in self.match_controller.matches:
            match_result = {
                "player1": match.player1,
                "player2": match.player2,
                "winner": match.winner
            }
            match_results.append(match_result)
        return match_results

    """ fonction pour charger un tournois"""
    def load_tournament(self):
        pass


    """ fonction pour lancer un round """

    """ fonction pour finir un round """

    """ fonction pour passer au round suivant"""

    """ fonction pour finir le tournois """

    """ fonction pour avoir acces a la liste des tournois existant """

    """ fonction pour supprimer un tournois"""
    def remove_tournament(self, tournament):
        if tournament in self.tournaments:
            self.tournaments.remove(tournament)
            print(f"Le tournoi {tournament.name_tournament} a été supprimé.")
        else:
            print("Le tournoi spécifié n'existe pas dans la liste des tournois.")