from models.round import Match
from controller.playercontroller import PlayerController
from datetime import datetime
from rich import print
import random


class RoundController:

    def __init__(self, tournament_controller):
        self.matches = []
        self.tournament_controller = tournament_controller
        self.player_controller = PlayerController()
        self.current_round_number = 0
        self.total_rounds = 4
        self.round_info = {}

    def add_match(self, player1, player2, color_player1, color_player2, round_number):
        """ Add a match to the tournament. """
        match = Match(player1, player2, color_player1, color_player2, round_number)
        self.matches.append(match)
        # Update players' played_with lists
        player1['played_with'].append(player2['national_chess_id'])
        player2['played_with'].append(player1['national_chess_id'])
        return match

    def display_round_results(self, round_number):
        """ This function prints the results of matches for a specific round. """
        print(f"\n[green]Résultats du Round {round_number}: [/]\n")
        round_matches = [match for match in self.matches if match.round_number == round_number]
        for match in round_matches:
            if match.winner is not None:
                winner_name = f"{match.winner['first_name']} {match.winner["last_name"]}"
            else:
                winner_name = "Égalité"
            print(f"{match.player1['first_name']} {match.player1['last_name']} "
                  f"vs {match.player2['first_name']} {match.player2['last_name']}: "
                  f"{winner_name}")

    def end_match(self, match, winner):
        """ This function concludes a match by specifying the winner and updating player scores accordingly. """
        match.winner = winner
        if winner:
            winner["score"] += 1
            # Determine the loser
            match.player1 if winner != match.player1 else match.player2
        else:
            # If the match is a draw, add 0.5 to each player
            for player in [match.player1, match.player2]:
                if player != match.winner:
                    player["score"] += 0.5

    def record_match_results(self, round_number, matches):
        """ Record the results of matches for a round. """
        self.current_round_number = round_number
        print(f"\n[green] Enregistrement des résultats du round {round_number} :[/green]")

        for match_index, match in enumerate(matches[:4], start=1):
            for player_index, player in enumerate([match.player1, match.player2], start=1):
                print(f"{player_index}. {player["first_name"]} {player["last_name"]}")
            while True:
                winner = input(f"Match {match_index}, Entrez numéro du vainqueur 1 ou 2, 'egalite' pour match nul, "
                               f"ou 'back' revenir en arrière) : ")
                if winner.lower() == 'egalite':
                    match.winner = None
                    self.end_match(match, None)
                    break
                elif winner.lower() == 'back':
                    break
                elif winner.strip():
                    winner = int(winner)
                    if winner == 1:
                        match.winner = match.player1
                        self.end_match(match, match.player1)
                        break
                    elif winner == 2:
                        match.winner = match.player2
                        self.end_match(match, match.player2)
                        break
                    else:
                        print("Numéro du joueur invalide. Veuillez réessayer")
                else:
                    print("Veuillez saisir un numero de joueur ou 'egalite' pour un match nul, "
                          "'back' pour revenir en arrière")
        print("Les résultats du round ont été enregistrés avec succès")

        self.display_round_results(round_number)
        end_time = datetime.now()
        print(f"\n[blue] Fin du round {round_number} - {end_time} [/blue]\n ")
        # Update information of round and match
        round_info = {
            "round_number": round_number,
            "matches": self.get_match_result(matches)
        }
        self.tournament_controller.update_round_info(round_number, round_info)
        # Update the JSON file
        self.tournament_controller.update_tournament_json("tournamentDB.json")

    def start_round(self, round_number):
        """
        This function initiates a round by selecting players, creating matches, displaying them,
        recording match results, and updating round information.
        """
        self.current_round_number = round_number
        while True:
            # For the first round, select players randomly
            if self.current_round_number == 1:
                tournament_players = self.tournament_controller.get_tournament_players()
                sorted_players = sorted(tournament_players, key=lambda x: x["score"], reverse=True)
                selected_players = random.sample(sorted_players, len(tournament_players))
            # For rounds 2 to 4
            elif self.current_round_number >= 2 and self.current_round_number <= 4:
                decision = input("Voulez-vous continuer oui/non (o/n) ? ").strip().lower()
                if decision == "n":
                    self.tournament_controller.update_tournament_json("tournamentDB.json")
                    print("Tournoi interrompu par l'utilisateur.")
                    break
                elif decision == "o":
                    tournament_players = self.tournament_controller.get_tournament_players()
                    sorted_players = sorted(tournament_players, key=lambda x: x["score"], reverse=True)
                    selected_players = sorted_players
                else:
                    print("Veuillez répondre par 'o' pour oui ou 'n' pour non.")
                    continue
            # If round number exceeds 4, end the tournament
            elif self.current_round_number > 4:
                break

            matches = self.create_matches(selected_players, self.current_round_number)
            self.display_matches(matches)
            self.record_match_results(self.current_round_number, matches)
            self.get_match_result(matches)
            self.current_round_number += 1

        return self.current_round_number

    def display_matches(self, matches):
        """ Display the players participating in each match. """
        for i, match in enumerate(matches, start=1):
            print(f"Match {i}: "
                  f"{match.player1['first_name']} {match.player1['last_name']} "
                  f"vs "
                  f"{match.player2['first_name']} {match.player2['last_name']}")

    def get_match_result(self, matches):
        """ This function collects the results of matches and returns them in a list of dictionaries. """
        match_results = []
        for match in matches:
            match_result = {
                "player1": match.player1,
                "player2": match.player2,
                "winner": match.winner
            }
            match_results.append(match_result)
        return match_results

    def create_matches(self, players, round_number):
        """
        This function creates matches between players for the specified round.
        Args:
        players (list): A list of player dictionaries.
        round_number (int): The number of the round.

        Returns:
        list: A list of Match objects representing the matches.
        """
        # Check if the number of players is even
        if len(self.tournament_controller.current_tournament.players) % 2 != 0:
            print("Le nombre de joueurs doit être pair pour former des paires pour les matchs")
            return []

        matches = []
        nb_matches = len(players)/2
        # Mark all players as unselected
        for i in range(0, len(players)):
            players[i]['selected'] = False

        # Iterate through the players, starting with index 0
        for i in range(0, len(players)):
            if players[i]['selected']:
                continue
            # Index j for the current player +1 to search for the next player
            j = i+1
            if j > len(players) - 1:
                j = 0

            # Select player 2
            match_player2 = players[j]
            stop = False

            while not stop:
                # Check if player1 hasn't played together or if player2 is different from player 1
                if (
                    (not players[i]['national_chess_id'] in match_player2['played_with'] or
                        len(matches) >= nb_matches - 1) and
                        match_player2['national_chess_id'] != players[i]['national_chess_id'] and
                        not match_player2['selected']
                ):
                    # Mark player as selected
                    match_player2['selected'] = True
                    players[i]['selected'] = True
                    # True when valid pair  - stop loop
                    stop = True
                # Pair is not valid
                else:
                    # Increment j
                    j += 1
                    # Check if j exceeds the list
                    if j >= len(players):
                        # Go back to the beginning of the list
                        j = 0
                        match_player2 = players[0]
                    else:
                        # j is within the list
                        match_player2 = players[j]

            # Create a match between player1 and player2
            match = self.add_match(players[i], match_player2, "white", "black", round_number)
            matches.append(match)
        return matches

    def check_round_complete(self, round_number):
        """ Check if all rounds have been completed. """
        if self.current_round_number >= self.total_rounds:
            return True
        return False
