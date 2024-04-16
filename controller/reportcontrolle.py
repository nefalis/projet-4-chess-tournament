from controller.tournamentcontroller import TournamentController
from view.tournamentview import TournamentView
from controller.roundcontroller import RoundController
from rich import print
from rich.table import Table
from rich.panel import Panel
from pprint import pprint

class ReportController:
    def __init__(self, tournament_controller):
        self.tournament_controller = TournamentController()
        self.tournament_controller.load_tournament("./data/tournamentDB.json")
        self.match_controller = RoundController(tournament_controller)

    """ fonction pour afficher TOUS les joueurs par ordre alphabetique """
    def display_all_player(self):
        players = self.tournament_controller.player_controller.get_players()
        players_sorted = sorted(players, key=lambda x: (x.last_name, x.first_name))

        table = Table(title="Liste de tous les joueurs par ordre alphabétique")
        table.add_column("Prénom", justify="left", style="cyan")
        table.add_column("Nom", justify="left", style="magenta")
        table.add_column("Date de naissance", justify="left", style="green")
        table.add_column("National chess id", justify="left", style="blue")
        for player in players_sorted:
            table.add_row(player.first_name,player.last_name, str(player.birthday), str(player.national_chess_id))
        print(table)

    """ fonction pour afficher la liste de TOUS les tournois """
    def display_all_tournament(self):
        tournaments = self.tournament_controller.get_tournaments()
        if tournaments:
            tournament_sorted = sorted(tournaments, key=lambda x: (x.name_tournament, x.date_start))
        
            table = Table(title="Liste de tous les tournois")
            table.add_column("Nom", justify="left", style="cyan")
            table.add_column("Date de début", justify="left", style="magenta")
            table.add_column("Date de fin", justify="left", style="green")
            table.add_column("Ville du tournoi", justify="left", style="blue")
            for tournament in tournament_sorted:
                table.add_row(tournament.name_tournament, str(tournament.date_start), str(tournament.date_finish), tournament.town_tournament)
            print(table)
        else:
            print("Aucun tournoi n'est disponible pour affichage.")

    """ fonction pour afficher les dates d'un tournoi """ 
    def display_tournament_date_report(self):   
        # Sélectionner un tournoi
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            print("Aucun tournoi sélectionné.")
            return
        # Créer un tableau pour afficher les informations du tournoi
        table_tournament_info = Table(title=f"Informations sur le tournoi {selected_tournament.name_tournament}")
        table_tournament_info.add_column("Nom", style="cyan")
        table_tournament_info.add_column("Date de début", style="orange_red1")
        table_tournament_info.add_column("Date de fin", style="green")
        table_tournament_info.add_column("Ville du tournoi", style="blue")
        table_tournament_info.add_row(selected_tournament.name_tournament,
                                        str(selected_tournament.date_start),
                                        str(selected_tournament.date_finish),
                                        selected_tournament.town_tournament)
        print(table_tournament_info)

    """ fonction pour afficher les joueurs d'un tournoi par ordre alphabétique """
    def display_tournament_player_report(self):
        # Sélectionner un tournoi
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            print("Aucun tournoi sélectionné.")
            return

        tournament_players = selected_tournament.players
        print(selected_tournament.players)
        if not tournament_players:
            print("Aucun joueur trouvé pour ce tournoi.")
            return

        players_sorted = sorted(tournament_players, key=lambda x: (x["last_name"], x["first_name"]))

        table = Table(title=f"Liste des joueurs par ordre alphabétique {selected_tournament.name_tournament}")
        table.add_column("Prénom", justify="left", style="cyan")
        table.add_column("Nom", justify="left", style="magenta")
        table.add_column("Score", justify="left", style="green")
        for player in players_sorted:
            table.add_row(player["first_name"], player["last_name"], str(player["score"]))
            
        print(table)

    """ fonction pour afficher les détails d'un tournoi"""
    def display_tournament_report(self):
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            print("Aucun tournoi sélectionné.")
            return
        
        # Créer un tableau pour afficher les informations du tournoi
        table_tournament_info = Table(title=f"Informations sur le tournoi {selected_tournament.name_tournament}")
        table_tournament_info.add_column("Nom", style="cyan")
        table_tournament_info.add_column("Date de début", style="orange_red1")
        table_tournament_info.add_column("Date de fin", style="green")
        table_tournament_info.add_column("Ville du tournoi", style="blue")
        table_tournament_info.add_column("Nombre de round", style="light_sea_green")
        table_tournament_info.add_row(selected_tournament.name_tournament,
                                        str(selected_tournament.date_start),
                                        str(selected_tournament.date_finish),
                                        str(selected_tournament.town_tournament),
                                        selected_tournament.number_round)
        print(table_tournament_info)
    
        if selected_tournament:
            for round_number, matches in selected_tournament():
                print(f"Détails du round : {round_number}")
                for match in matches:
                    winner_name = match.winner["first_name"] + " " + match.winner["last_name"] if match.winner else "Égalité"
                    print(f"Match : {match.player1['first_name']} {match.player1['last_name']} vs {match.player2['first_name']} {match.player2['last_name']}, Vainqueur : {winner_name}")