
import json
import os
from datetime import datetime
from controller.roundcontroller import RoundController
from controller.playercontroller import PlayerController
from view.tournamentview import TournamentView
from models.tournament import Tournament
from rich import print
import random
from pprint import pprint

class TournamentController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_model = Tournament
        self.current_tournament = None
        self.match_controller = RoundController(self)
        self.tournaments = []
        self.round_count = 0
        self.current_round_number = 0
        self.round_info = {}

    """ fonction pour creer un tournois"""
    def create_tournament(self, name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament):
        new_tournament = Tournament(name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament, players=[])
        # Assigner le nouveau tournoi à la variable current_tournament
        self.current_tournament = new_tournament  
        # Ajoutez le nouveau tournoi à la liste
        self.tournaments.append(new_tournament)
        self.update_tournament_json("tournamentDB.json")  
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
        # Écrivez les données dans le fichier JSON
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump(tournaments_data, json_file, indent=4, ensure_ascii=False, default=str)

    """ fonction pour charger un tournois"""
    def load_tournament(self, filename):
        try:
            with open(filename, 'r') as file:
                tournaments_data = json.load(file)
                self.tournaments = [Tournament(tournament_data["name_tournament"], tournament_data["town_tournament"], tournament_data["date_start"], tournament_data["date_finish"], tournament_data["number_round"], tournament_data["number_player"], tournament_data["description_tournament"], tournament_data["players"]) for tournament_data in tournaments_data]
        except FileNotFoundError:
            print(f"Le fichier {filename} n'a pas été trouvé")
        except json.JSONDecodeError:
            print(f"Erreur lors du décodage du fichier JSON {filename}")
    
    """ fonction pour ajouter des joueurs au tournois"""
    def add_player_tournament(self, selected_players):
        if self.current_tournament is None:
            print("Aucun tournoi en cours")
            return
        for player in (selected_players):
            self.current_tournament.add_player(player)

    """ fonction pour commencer un tournois"""
    def start_tournament(self):
        tournament = TournamentView.select_tournament(self)
        print(f"\n[blue] Vous allez commencer le tournoi {tournament.name_tournament}[/blue]\n")
        if tournament is None:
            print("Aucun tournoi sélectionné")
            return
        print(f"Heure du début: {datetime.now()}")
        self.current_tournament = tournament
        self.current_tournament.players = self.get_tournament_players()
        round_number = 1

        while round_number <= 4:
            # Commencer un nouveau round
            self.match_controller.start_round(round_number)
            # Enregistrer les résultats du round
            # self.match_controller.record_match_results(round_number, matches)
            # self.match_controller.get_match_result()
            # Incrémenter le compteur de rounds
            self.round_count += 1
            # Passer au round suivant
            round_number += 1

        # Une fois que tous les rounds sont terminés, finir le tournoi
        # end_time = datetime.now()
        # tournament.end_time = end_time
        self.end_tournament()   

        self.update_tournament_json("tournamentDB.json")
        
    """ fonction pour donner le score final des joueurs a la fin du tournoi """
    def end_score_player(self):
        player_scores = {}
        # Parcourir les tournois pour récupérer les données des joueurs
        for player_data in self.current_tournament.players:
            # Vérifier si player_data est un dictionnaire
            if isinstance(player_data, dict):
                player_name = f"{player_data['first_name']} {player_data['last_name']}"
                player_score = player_data['score']
                if player_name in player_scores:
                    player_scores[player_name] += player_score
                else:
                    player_scores[player_name] = player_score
            else:
                print("Erreur: player_data n'est pas un dictionnaire.")
        return player_scores
    
    """ fonction pour voir les joueurs du tournoi """
    def get_tournament_players(self):
        tournament_players = self.current_tournament.players
   
        return tournament_players
    
    """ fonction pour avoir les tournois"""
    def get_tournaments(tournament_controller):
        print("tc l118 get tournament")
        print(tournament_controller.tournaments)
        return tournament_controller.tournaments
    
    """ fonction pour enregistrer les information des rounds """
    def update_round_info(self, round_number, round_info):
        self.round_info[round_number] = round_info

    def get_round_info(self):
        print("pouezt info l 140 tc")
        return self.round_info
    
    """ fonction pour afficher la liste des tournois """
    def display_tournament(tournament_controller):
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")
    
    """ fonction pour choisir des joueurs aléatoire """
    def choose_random_players(self):
        if len(self.current_tournament.players) % 2 != 0:   
            print("Le nombre de joueurs doit être pair pour former des paires pour les matchs")
            return []
        random_players = random.sample(self.current_tournament.players, len(self.current_tournament.players))
        return random_players


    """ fonction pour finir le tournois """
    def end_tournament(self):
        winner_name = None
        winner_score = None

        if self.match_controller.check_round_complete(self.match_controller.current_round_number):
            player_scores = self.end_score_player()
            if player_scores:
                # Trier les joueurs par score (le plus haut d'abord)
                sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
                # Afficher le classement des joueurs
                print(f"\n[green]Classement des joueurs:[/green]")
                for rank, (player_name, score) in enumerate(sorted_players, start=1):
                    print(f"{rank}. {player_name} - Score: {score} points")
                # Déterminer le vainqueur
                winner_name, winner_score = sorted_players[0] if sorted_players else (None, None)
                if winner_name:
                    # Afficher le vainqueur
                    print(f"\n[yellow]Le vainqueur du tournoi est : {winner_name} avec un score de {winner_score} points[/yellow]")
            else:
                print("Aucun joueur n'a participé au tournoi ou n'a marqué de points.")
        else:
            print("Le tournoi ne peut pas être terminé car tous les rounds n'ont pas été joués") 

        # Terminer le tournoi en définissant la date et l'heure de fin
        # end_time = datetime.now()
        # print(f"\n[blue]Le tournoi est terminé.[/blue]")
        # print(f"[blue]Date et heure de fin : {end_time}[/blue]\n")

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
        

