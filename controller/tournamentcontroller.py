
import json
import os
from datetime import datetime
from controller.roundcontroller import RoundController
from controller.playercontroller import PlayerController
from view.tournamentview import TournamentView
from models.tournament import Tournament
import random
from datetime import datetime

class TournamentController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_model = Tournament
        self.current_tournament = None
        self.match_controller = RoundController(self)
        self.tournaments = []
        self.test = []
        self.round_count = 0
        self.current_round_number = 0

    """ fonction pour creer un tournois"""
    def create_tournament(self, name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament):
        new_tournament = self.tournament_model(name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament, players=[])
        # Assigner le nouveau tournoi à la variable current_tournament
        self.current_tournament = new_tournament  
        # Ajoutez le nouveau tournoi à la liste
        self.tournaments.append(new_tournament)
        self.update_tournament_json("tounamentDB.json")  
        print("l26 tourcontrol - nouveau tournoi")
        return new_tournament
    
    """ fonction pour creer un fichier json"""
    def create_tournament_json(self, filename):
        data_folder = "data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        full_path = os.path.join(data_folder, filename)
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                tournaments_data = json.load(f)
                self.tournaments = [Tournament(**tournament_data) for tournament_data in tournaments_data]

    """ fonction pour mettre a jour le fichier json """
    def update_tournament_json(self, filename):
        data_folder = "data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        full_path = os.path.join(data_folder, filename)    
        # Récupérez les données du tournoi
        tournaments_data = [tournament.__dict__ for tournament in self.tournaments]
        print("Données du tournoi à enregistrer :", tournaments_data)
        # Écrivez les données dans le fichier JSON
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump(tournaments_data, json_file, indent=4, ensure_ascii=False)
    
    """ fonction pour ajouter des joueurs au tournois"""
    def add_player_tournament(self, players):
        self.test = players
        if self.current_tournament is None:
            print("l60 tourcontrol - Aucun tournoi en cours")
            return
        for player in players:
            self.current_tournament.add_player(player)

    """ fonction pour commencer un tournois"""
    def start_tournament(self):
        tournament = TournamentView.select_tournament(self)
        print(f"Vous allez commencer le tournoi {tournament.name_tournament}")
        if tournament is None:
            print("Aucun tournoi sélectionné")
            return
        start_time = datetime.now()
        tournament.start_time = start_time
        print(f"Le tournoi {tournament.name_tournament} démarre à: {start_time}")
        self.current_tournament = tournament

        round_number = 1

        while round_number <= 4:
            # Commencer un nouveau round
            self.match_controller.start_round(round_number)
            # Enregistrer les résultats du round
            self.match_controller.record_match_results(round_number)
            # Incrémenter le compteur de rounds
            self.round_count += 1
            # Passer au round suivant
            round_number += 1

        # Une fois que tous les rounds sont terminés, finir le tournoi
        self.end_tournament(datetime.now())

        # self.match_controller.start_round(round_number)
        # self.match_controller.record_match_results(round_number)
        


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

    """ fonction pour finir le tournois """
    def end_tournament(self, end_time):
        if self.match_controller.check_round_complete(self.current_round_number):
            player_scores = {}
            for tournament in self.tournaments:
                for player in tournament.players:
                    if player.first_name not in player_scores:
                        player_scores[player.first_name] [player.last_name] = 0
                    player_scores[player.first_name] [player.last_name] += player.score

            # Déterminer le joueur avec le score le plus élevé comme vainqueur
            winner_name = max(player_scores, key=player_scores.get)
            winner_score = player_scores[winner_name]

            # Afficher le vainqueur
            print(f"Le vainqueur du tournoi est : {winner_name} avec un score de {winner_score} points")
        else:
            print("l128 tc Le tournoi ne peut pas être terminé car tous les rounds n'ont pas été joués") 

        # Terminer le tournoi en définissant la date et l'heure de fin
        end_time = datetime.now()
        self.current_tournament.end_tournament(end_time)
        print(" l133 tc Le tournoi est terminé.")
        print("Date et heure de fin :", end_time)

    # Terminer le tournoi en définissant la date et l'heure de fin
        end_time = datetime.now()
        self.current_tournament.end_tournament(end_time)
        print("l105 tourcontrol - Le tournoi est terminé")
        print("Date et heure de fin :", end_time)

    """ fonction pour charger un tournois"""
    def load_tournament(self):
        pass

    """ fonction pour afficher la liste des tournois """
    def display_tournament(tournament_controller):
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")

    """ pour rechercher un tournoi specifique"""
    def get_tournament_by_name(self, name_tournament, date_start):
        for tournament in self.tournaments:
            if tournament.name_tournament == name_tournament and tournament.date_start == date_start:
                return tournament
        return None

    """ fonction pour supprimer un tournois"""
    def remove_tournament(self, tournament):
        if tournament in self.tournaments:
            self.tournaments.remove(tournament)
            print(f"Le tournoi {tournament.name_tournament} a été supprimé")
        else:
            print("Le tournoi spécifié n'existe pas dans la liste des tournois")


        # """ fonction pour verifer que tout les round ont été fait """
    # def check_round_complete(self):
    #     played_round = set()
    #     for match in self.match_controller.matches:
    #         played_round.add(match.round_number)
    #     return len(played_round) == 4

        # """ fonction pour démarrer un tournois"""
    # def start_round(self):
    #     print(f"Round 1 {datetime.now}")
    #     all_players = self.player_controller.get_players()
    #     print("l73 tc all_player")
    #     if len(all_players) < 8:
    #         print("Il n'y a pas assez de joueurs pour commencer un tour")
    #         return
    #     # Choisissez 8 joueurs aléatoires pour le round
    #     round_players = random.sample(all_players, 8)
    #     random.shuffle(round_players)
    #     # Creation des matchs du round
    #     matches = self.match_controller.create_matches(round_players)
    #     # Afficher les paires de joueurs
    #     self.match_controller.display_matches(matches)
        

