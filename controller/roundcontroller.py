from models.round import Match
from controller.playercontroller import PlayerController
from datetime import datetime
from rich import print
import random
from pprint import pprint

class RoundController:

    def __init__(self, tournament_controller):
        self.matches = []
        self.tournament_controller = tournament_controller
        self.player_controller = PlayerController()
        self.current_round_number = 0
        self.total_rounds = 4

    def add_match(self, player1, player2, color_player1, color_player2, round_number):
        match = Match(player1, player2, color_player1, color_player2, round_number)
        self.matches.append(match)
        return match


    """ fonction pour afficher les resultats apres chaque round"""
    def display_round_results(self, round_number):
        print(f"\n[green]Résultats du Round {round_number}: [/]\n")
        for match in self.matches[:4]:
            if match.winner is not None :
                winner_name = f"{match.winner['first_name']} {match.winner["last_name"]}"
            else:
                winner_name = "Égalité"

            print(f"{match.player1['first_name']} {match.player1['last_name']} vs {match.player2['first_name']} {match.player2['last_name']}: {winner_name}")

    # """ pour mettre a jour les rangs"""
    # def update_score(self, matches):
    #     for match in matches:
    #         self.end_match(match, match.winner)
    #     self.tournament_controller.update_tournament_json("tournamentDB.json")
    #     print("Le score des joueurs a été mis à jour dans le fichier JSON.")

    def end_match(self, match, winner):
        match.winner = winner
        if winner:
            print(f"j'ajoute 1 au gagnant {winner}")
            winner["score"] += 1  
            # Déterminez le perdant et mettez à jour son score à 0
            loser = match.player1 if winner != match.player1 else match.player2
            print(f"j'ajoute 0 au perdant {loser}")
            loser["score"] = 0
        else:
            # Si le match égalité, ajoutez 0.5 à chaque joueur
            for player in [match.player1, match.player2]:
                if player != match.winner:
                    print("je met 0.5 au 2")
                    player["score"] += 0.5

    """ fonction pour enregistrer les résultat du round """
    def record_match_results(self, round_number, matches):
        self.current_round_number = round_number 
        print(f"\n[green]Enregistrement des résultats du round {round_number} :[/green]")
        
        for match_index, match in enumerate(matches[:4], start=1):
            print(f"Match {match_index}:")
            for player_index, player in enumerate([match.player1, match.player2], start=1):
                print(f"{player_index}. {player["first_name"]} {player["last_name"]}")
            while True:
                winner = input(f"Match {match_index}, Vainqueur (entrez numéro du vainqueur (1 ou 2), 'egalite' pour match nul, ou 'back' revenir en arrière) : ")
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
                    print("Veuillez saisir un numero de joueur ou 'egalite' pour un match nul, ou 'back' pour revenir en arrière")

        print("Les résultats du round ont été enregistrés avec succès")

        # Afficher les résultats du round
        self.display_round_results(round_number)
        end_time = datetime.now()
        print(f"\n[blue] Fin du round {round_number} - {end_time} [/blue]")

        # Mettre à jour les informations du tour et les résultats des matchs
        round_info = {
            "round_number": round_number,
            "matches": self.get_match_result(matches)  
        }
        self.tournament_controller.update_round_info(round_number, round_info)

        # Mettre à jour le fichier JSON
        self.tournament_controller.update_tournament_json("tournamentDB.json")

        print(self.tournament_controller.round_info)
    
    """ fonction pour démarrer un tournois"""
    def start_round(self, round_number):
        self.current_round_number = round_number 
        start_time = datetime.now()
        print(f"[blue]\n Round {round_number} - {start_time} [/blue]\n")
        
        # je recupere les joueurs
        tournament_players = self.tournament_controller.get_tournament_players()
        # je trie les joueurs
        sorted_players = sorted(tournament_players, key=lambda x: x["score"], reverse=True)
        # je verifie si round supérieur a 1
        # si oui on choisit au hasard
        # si non on choisit par score et on verif si ils ont deja joué ensemble
        if round_number > 1:
            selected_players = sorted_players
        else :
            selected_players = random.sample(sorted_players, len(tournament_players))
        # debut match (create_matches ? )
        matches = []
        matches = self.create_matches(selected_players, round_number)
        self.display_matches(matches)
        self.record_match_results(round_number, matches)
        self.get_match_result(matches)
            
        #     for i in range(0, len(sorted_players), 2):
        #         if i + 1 < len(sorted_players):
        #             match_pairs.append({"player1": sorted_players[i], "player2": sorted_players[i + 1]})

    """ fonction pour afficher les joueurs des matchs"""
    def display_matches(self, matches):
        for i, match in enumerate(matches, start=1):
            print( f"Match {i}: {match.player1['first_name']} {match.player1['last_name']} vs {match.player2['first_name']} {match.player2['last_name']} ")
    
    """ fonction pour collecter les resultats des matchs """
    def get_match_result(self, matches):
        match_results = []
        for match in matches:
            match_result = {
                "player1": match.player1,
                "player2": match.player2,
                "winner": match.winner
            }
            match_results.append(match_result)
        return match_results

    """ fonction pour creer les matchs pour 1 round  """
    def create_matches(self, players, round_number):
        matches =[]
        if len(self.tournament_controller.current_tournament.players) % 2 != 0:   
            print("Le nombre de joueurs doit être pair pour former des paires pour les matchs")
            return []
        
        for i in range(0, len(players) - 1, 2):
        # Vérifiez si l'index suivant dépasse la limite de la liste
            if i + 1 < len(players):
                match = self.add_match(players[i], players[i + 1], "white", "black", round_number)
                matches.append(match)
        return matches


    """ fonction pour verifier que tout les round ont été fait """
    def check_round_complete(self, round_number):
        if self.current_round_number >= self.total_rounds:
            return True
        return False
    

    # """ fonction pour passer au round suivant """
    # def next_round(self):
    #     round_number = self.current_round_number
    #     if self.check_round_completion(round_number):
    #         print("Les matchs du round en cours ont été joués")
    #         next_round_number = round_number + 1  
    #         self.start_round(next_round_number)
    #     else:
    #         print("Les matchs du round en cours n'ont pas encore été joués")

    # """ fonction pour verifier si tous les matchs du round ont été joué """
    # def check_round_completion(self):
    #     if len(self.matches) == 4:
    #         for match in self.matches:
    #             if match.winner is None:
    #                 return False
    #         return True
    #     return False

    # """ fonction pour demarrer le tournoi """
    # def start_tournament_round(self):
    #     tournament = TournamentView.select_tournament(self.tournament_controller)
    #     print(f"Vous allez commencer le tournoi {tournament.name_tournament}")
    #     if tournament is None:
    #         print("Aucun tournoi sélectionné")
    #         return
    #     start_time = datetime.now()
    #     tournament.start_time = start_time
    #     print(f"Le tournoi {tournament.name_tournament} démarre à: {start_time}")
    #     self.tournament_controller.current_tournament = tournament
    #     self.tournament_controller.start_round()

    # """ fonction pour demarrer le 1er round """
    # def start_first_round(self):
    #     # verifier si il y a un tournoi en cours
    #     if self.tournament_controller.current_tournament is None:
    #         print("Aucun tournoi en cours")
    #         return
    #     # verifier si il y a assez de joueur
    #     if len(self.tournament_controller.current_tournament.players) < 8:
    #         print("Pas assez de joueurs pour démarrer le premier round.")
    #         return
    #     # Générer les matchs pour le premier round
    #     round_players = self.tournament_controller.current_tournament.players[:8]
    #     for i in range(0, len(round_players), 2):
    #         match = self.tournament_controller.add_match(round_players[i], round_players[i + 1], "white", "black")
    #         match.start_match()
    #     print("Le premier round du tournoi a démarré avec succès")