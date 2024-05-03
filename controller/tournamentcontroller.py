
import json
import os
from datetime import datetime
from controller.roundcontroller import RoundController
from controller.playercontroller import PlayerController
from view.tournamentview import TournamentView
from models.tournament import Tournament


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

    def create_tournament(self, name_tournament, town_tournament, date_start, date_finish,
                          number_player, description_tournament, rounds_info):
        """ Create a new tournament and then add to the tournament database. """
        new_tournament = Tournament(
            name_tournament,
            town_tournament,
            date_start,
            date_finish,
            number_player,
            description_tournament,
            rounds_info,
            players=[]
        )
        # Assign the new tournament to the variable current_tournament
        self.current_tournament = new_tournament
        # Add the new tournament to the list of tournaments
        self.tournaments.append(new_tournament)
        self.update_tournament_json("tournamentDB.json")
        return new_tournament

    def create_tournament_json(self, filename):
        """ Create tournament database from a JSON file  """
        data_folder = "data"
        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        # Construct the full path to the JSON file
        full_path = os.path.join(data_folder, filename)
        # Check if the JSON file exists
        if os.path.exists(full_path):
            # If it exists, load the player data from the file
            with open(full_path, 'r') as f:
                tournaments_data = json.load(f)
                self.tournaments = [Tournament(**tournament_data) for tournament_data in tournaments_data]

    def update_tournament_json(self, filename):
        """ Update a JSON file with tournament data. """
        data_folder = "data"
        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        # Construct the full path to the JSON file
        full_path = os.path.join(data_folder, filename)
        # Ajouter les informations sur les rounds
        tournaments_data = [tournament.__dict__ for tournament in self.tournaments]
        for tournament_data in tournaments_data:
            # Ajouter les informations sur les rounds dans chaque tournoi
            rounds_info = self.get_round_info()
            formatted_rounds = self.format_rounds_info(rounds_info)
            tournament_data["rounds_info"] = formatted_rounds

        # write player data to the JSON file
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump(tournaments_data, json_file, indent=4, ensure_ascii=False, default=str)

    def format_rounds_info(self, rounds_info):
        """
        Format round information to include in the JSON file.
        """
        formatted_rounds = {}
        for round_number, round_data in rounds_info.items():
            formatted_round = {}
            formatted_round["round"] = round_number
            # Add match information
            formatted_matches = []
            for match_info in round_data["matches"]:
                formatted_match = {}
                formatted_match["player1"] = (
                    f"{match_info['player1']['first_name']} "
                    f"{match_info['player1']['last_name']}"
                )
                formatted_match["player2"] = (
                    f"{match_info['player2']['first_name']} "
                    f"{match_info['player2']['last_name']}"
                )
                formatted_match["winner"] = f"{match_info['winner']['first_name']} {match_info['winner']['last_name']}"
                formatted_matches.append(formatted_match)
            formatted_round["matches"] = formatted_matches
            formatted_rounds[round_number] = formatted_round
        return formatted_rounds

    def load_tournament(self, filename):
        """ Load tournament data from a JSON file. """
        try:
            with open(filename, 'r') as file:
                # Load tournament data from the file
                tournaments_data = json.load(file)
                self.tournaments = [
                    Tournament(
                        tournament_data["name_tournament"],
                        tournament_data["town_tournament"],
                        tournament_data["date_start"],
                        tournament_data["date_finish"],
                        tournament_data["number_player"],
                        tournament_data["description_tournament"],
                        tournament_data["rounds_info"],
                        tournament_data["players"]
                    )
                    for tournament_data in tournaments_data
                ]
        except FileNotFoundError:
            TournamentView.print_controller_tournament(0)
        except json.JSONDecodeError:
            TournamentView.print_controller_tournament(1)

    def add_player_tournament(self, selected_players):
        """ Add players to the current tournament. """
        if self.current_tournament is None:
            TournamentView.print_controller_tournament(2)
            return
        # Add each selected player to the current tournament
        for player in (selected_players):
            self.current_tournament.add_player(player)

    def start_tournament(self):
        """
        Start a tournament.
        This function selects a tournament, starts its rounds, and updates the tournament JSON file.
        """
        # Select a tournament to start
        tournament = TournamentView.select_tournament(self)
        TournamentView.print_controller_tournament_param(tournament, 5)
        # Check if a tournament is selected
        if tournament is None:
            TournamentView.print_controller_tournament(3)
            return
        TournamentView.print_controller_tournament_param(datetime.now(), 0)
        # Set the current tournament
        self.current_tournament = tournament
        # Get players for the tournament
        self.current_tournament.players = self.get_tournament_players()
        round_number = 1

        # Start a new round
        self.round_count = self.match_controller.start_round(round_number)
        # Finish the tournament once all rounds are completed
        self.end_tournament()
        # Update the tournament JSON file
        self.update_tournament_json("tournamentDB.json")

    def end_score_player(self):
        """ Calculate the final scores of players at the end of the tournament. """
        player_scores = {}
        # Iterate through the players of the current tournament to retrieve their data
        for player_data in self.current_tournament.players:
            # Check if player_data is a dictionary
            if isinstance(player_data, dict):
                player_name = f"{player_data['first_name']} {player_data['last_name']}"
                player_score = player_data['score']
                # Update the player's score in the player_scores dictionary
                if player_name in player_scores:
                    player_scores[player_name] += player_score
                else:
                    player_scores[player_name] = player_score
            else:
                TournamentView.print_controller_tournament(4)
        return player_scores

    def get_tournament_players(self):
        """ Get the players of the current tournament. """
        tournament_players = self.current_tournament.players
        return tournament_players

    def update_round_info(self, round_number, round_info):
        """ This function updates the information of a specific round. """
        self.round_info[round_number] = round_info

    def get_round_info(self):
        """ This function retrieves the information of all rounds. """
        return self.round_info

    def get_tournaments(tournament_controller):
        """ Get the list of tournaments. """
        return tournament_controller.tournaments

    def display_tournament(tournament_controller):
        """ Display the list of tournaments. """
        TournamentView.print_controller_tournament(5)
        for tournament in tournament_controller.tournaments:
            TournamentView.print_controller_tournament_param([tournament], 1)

    def end_tournament(self):
        """ This function concludes the tournament by displaying the player rankings and determining the winner. """
        winner_name = None
        winner_score = None

        if self.match_controller.check_round_complete(self.match_controller.current_round_number):
            player_scores = self.end_score_player()
            if player_scores:
                # Sort players by score (highest first)
                sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
                # Display player rankings
                TournamentView.print_controller_tournament(6)
                for rank, (player_name, score) in enumerate(sorted_players, start=1):
                    TournamentView.print_controller_tournament_param([rank, player_name, score], 2)
                # Determine the winner
                winner_name, winner_score = sorted_players[0] if sorted_players else (None, None)
                if winner_name:
                    # Display the winner
                    TournamentView.print_controller_tournament_param([winner_name, winner_score], 3)
            else:
                TournamentView.print_controller_tournament(7)
        else:
            TournamentView.print_controller_tournament(8)
        self.current_tournament.rounds_info = self.get_round_info()

    def get_tournament_by_name(self, name_tournament, date_start):
        """ Retrieve a specific tournament - name and start date. """
        for tournament in self.tournaments:
            if tournament.name_tournament == name_tournament and tournament.date_start == date_start:
                return tournament
        return None

    """ fonction pour supprimer un tournois"""
    def remove_tournament(self, tournament):
        """ Remove a tournament from the list of tournaments. """
        if tournament in self.tournaments:
            self.tournaments.remove(tournament)
        else:
            TournamentView.print_controller_tournament(10)

    def resume_tournament(self):
        """
        Load tournament data from the JSON file and resume the tournament.
        """
        filename = "tournamentDB.json"

        # Load tournament data from the JSON file.
        try:
            self.load_tournament(filename)
        except FileNotFoundError:
            TournamentView.print_controller_tournament(0)
            return
        except json.JSONDecodeError:
            TournamentView.print_controller_tournament(1)
            return

        # Display available tournaments for resume.
        self.display_tournament()
        # Ask the user to choose a tournament to resume.
        selected_tournament_name = TournamentView.print_controller_tournament(12)
        selected_tournament_date = TournamentView.print_controller_tournament(13)
        # Retrieve the selected tournament.
        selected_tournament = self.get_tournament_by_name(selected_tournament_name, selected_tournament_date)
        # Check if the selected tournament exists.
        if selected_tournament is None:
            TournamentView.print_controller_tournament(10)
            return

        self.current_tournament = selected_tournament
        # Check if all rounds are completed.
        total_rounds = 4
        last_round_number = max(self.current_tournament.rounds_info.keys(), default=0)
        if last_round_number == total_rounds:
            TournamentView.print_controller_tournament(11)
            return

        # Start the tournament from the next round after the last recorded round.
        next_round_number = int(last_round_number) + 1
        TournamentView.print_controller_tournament_param(next_round_number, 4)
        self.match_controller.start_round(next_round_number)
        # Finish the tournament.
        self.end_tournament()
        # Update the tournament JSON file.
        self.update_tournament_json("tournamentDB.json")
