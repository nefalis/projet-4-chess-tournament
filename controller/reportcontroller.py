from controller.tournamentcontroller import TournamentController
from view.tournamentview import TournamentView
from view.reportview import ReportView
from controller.roundcontroller import RoundController
from rich.table import Table


class ReportController:
    def __init__(self, tournament_controller):
        self.tournament_controller = TournamentController()
        self.tournament_controller.load_tournament("./data/tournamentDB.json")
        self.match_controller = RoundController(tournament_controller)
        self.round_info = {}

    def display_all_player(self):
        """ Display all players in alphabetical order """
        # Retrieve all players from the players controller
        players = self.tournament_controller.player_controller.get_players()
        # Sort players alphabetically by last name and first name
        players_sorted = sorted(players, key=lambda x: (x.last_name, x.first_name))

        # Create a formatted table
        table = Table(title="\n Liste de tous les joueurs par ordre alphabétique")
        table.add_column("Prénom", justify="left", style="cyan")
        table.add_column("Nom", justify="left", style="magenta")
        table.add_column("Date de naissance", justify="left", style="green")
        table.add_column("National chess id", justify="left", style="blue")
        for player in players_sorted:
            table.add_row(player.first_name, player.last_name, str(player.birthday), str(player.national_chess_id))
        ReportView.print_controller_report_param(table, 0)

    def display_all_tournament(self):
        """ Display the list of all tournaments """
        # Retrieve all tournaments from the tournament controller
        tournaments = self.tournament_controller.get_tournaments()
        if tournaments:
            # Sort tournaments alphabetically by tournament name and date of start
            tournament_sorted = sorted(tournaments, key=lambda x: (x.name_tournament, x.date_start))
            # Create a formatted table
            table = Table(title="\n Liste de tous les tournois")
            table.add_column("Nom", justify="left", style="cyan")
            table.add_column("Date de début", justify="left", style="magenta")
            table.add_column("Date de fin", justify="left", style="green")
            table.add_column("Ville du tournoi", justify="left", style="blue")
            for tournament in tournament_sorted:
                table.add_row(
                    tournament.name_tournament,
                    str(tournament.date_start),
                    str(tournament.date_finish),
                    tournament.town_tournament
                )
            ReportView.print_controller_report_param(table, 0)
        else:
            ReportView.print_controller_report(0)

    def display_tournament_date_report(self):
        """ Display the dates of a tournament. """
        # Select a tournament
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            ReportView.print_controller_report(1)
            return
        # Create a table to display tournament information
        table_tournament_info = Table(title=f"\n Informations sur le tournoi {selected_tournament.name_tournament}")
        table_tournament_info.add_column("Nom", style="cyan")
        table_tournament_info.add_column("Date de début", style="orange_red1")
        table_tournament_info.add_column("Date de fin", style="green")
        table_tournament_info.add_column("Ville du tournoi", style="blue")
        table_tournament_info.add_row(
            selected_tournament.name_tournament,
            str(selected_tournament.date_start),
            str(selected_tournament.date_finish),
            selected_tournament.town_tournament
        )
        ReportView.print_controller_report_param(table_tournament_info, 0)

    def display_tournament_player_report(self):
        """ Display players of a tournament in alphabetical order. """
        # Select a tournament
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            ReportView.print_controller_report(1)
            return

        # Get the players of the selected tournament
        tournament_players = selected_tournament.players
        if not tournament_players:
            ReportView.print_controller_report(2)
            return

        # Sort tournament players alphabetically by last name and first name
        players_sorted = sorted(tournament_players, key=lambda x: (x["last_name"], x["first_name"]))
        # Create a table to display players information
        table = Table(title=f"\n Liste des joueurs par ordre alphabétique {selected_tournament.name_tournament}")
        table.add_column("Prénom", justify="left", style="cyan")
        table.add_column("Nom", justify="left", style="magenta")
        table.add_column("Score", justify="left", style="green")
        for player in players_sorted:
            table.add_row(player["first_name"], player["last_name"], str(player["score"]))
        ReportView.print_controller_report_param(table, 0)

    def display_tournament_report(self):
        """
        Display the details of a selected tournament including tournament information,
        player scores, the winner of the tournament, and details of each round's matches.
        """
        selected_tournament = TournamentView.select_tournament(self.tournament_controller)
        if selected_tournament is None:
            ReportView.print_controller_report(1)
            return

        # Create an array to display tournament information
        table_tournament_info = Table(title=f"\n Informations sur le tournoi {selected_tournament.name_tournament}")
        table_tournament_info.add_column("Nom", style="cyan")
        table_tournament_info.add_column("Date de début", style="orange_red1")
        table_tournament_info.add_column("Date de fin", style="green")
        table_tournament_info.add_column("Ville du tournoi", style="blue")
        table_tournament_info.add_row(
            selected_tournament.name_tournament,
            str(selected_tournament.date_start),
            str(selected_tournament.date_finish),
            str(selected_tournament.town_tournament)
            )
        ReportView.print_controller_report_param(table_tournament_info, 0)

        # Create an array to display player score information.
        table_tournament_info_player = Table(title="\n Score des joueurs du tournoi ")
        table_tournament_info_player.add_column("Prénom", style="cyan")
        table_tournament_info_player.add_column("Nom", style="green")
        table_tournament_info_player.add_column("Score", style="dark_sea_green")

        # Sort the players by score.
        tournament_players = selected_tournament.players
        players_sorted = sorted(tournament_players, key=lambda x: x["score"], reverse=True)

        # Iterate over each player in the tournament's player list.
        for player_data in players_sorted:
            table_tournament_info_player.add_row(
                player_data["first_name"],
                player_data["last_name"],
                str(player_data["score"])
            )
        ReportView.print_controller_report_param(table_tournament_info_player, 0)

        winner = players_sorted[0]
        # Display the name of the winning player.
        ReportView.print_controller_report_param(winner, 1)

        # Display the details of the rounds.
        rounds_info = selected_tournament.rounds_info
        for round_number, round_info in rounds_info.items():
            round_table = Table(title=f"\n Round {round_info['round']} - Matchs")
            round_table.add_column("Match", justify="center", style="cyan")
            round_table.add_column("Joueur 1", style="dark_red")
            round_table.add_column("Joueur 2", style="dark_goldenrod")
            round_table.add_column("Vainqueur", style="dark_orange3")

            for match_number, match in enumerate(round_info["matches"], start=1):
                round_table.add_row(
                    str(match_number),
                    match["player1"],
                    match["player2"],
                    match["winner"]
                )
            ReportView.print_controller_report_param(round_table, 0)
