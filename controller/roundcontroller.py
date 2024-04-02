from models.round import Match
from controller.playercontroller import PlayerController
from datetime import datetime
from models.player import Player
import random
import json

class RoundController:

    def __init__(self, tournament_controller):
        self.matches = []
        self.tournament_controller = tournament_controller
        self.player_controller = PlayerController()
        self.current_round_number = 0

    def add_match(self, player1, player2, color_player1, color_player2, round_number):
        # match = Match(player1, player2, color_player1, color_player2, round_number)
        # self.matches.append(match)
        # return match
        player1_obj = player1
        player2_obj = player2
        match = Match(player1_obj, player2_obj, color_player1, color_player2, round_number)
        self.matches.append(match)
        return match
    

    def end_match(self, match, winner):
        match.winner = winner
        # Mettre à jour les joueurs avec le résultat du match
        if winner:
            # Incrémente le score du joueur gagnant
            winner.score += 1  
            # Déterminez le perdant et mettez à jour son score à 0
            loser = match.player1 if winner != match.player1 else match.player2
            loser.score = 0
        else:
            # Si le match se termine par une égalité, ajoutez 0.5 à chaque joueur
            for player in [match.player1, match.player2]:
                player.score += 0.5

    """ fonction pour enregistrer les résultat du 1er round """
    def record_match_results(self, round_number):
        print(f"Enregistrement des résultats du round {round_number} :")
        for match in self.matches[:4]:
            print(f"Match : {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}")
            while True:
                winner = input("Vainqueur (entrez le prenom du vainqueur, 'egalite' pour un match nul, ou 'back' pour revenir en arrière) : ")
                if winner.lower() == 'egalite':
                    self.end_match(match, None)
                    break
                # pour revenir en arriere
                elif winner.lower() == 'back':
                    break 
                elif winner.strip():  
                    if winner == match.player1.first_name:
                        self.end_match(match, match.player1)
                        self.player_controller.update_score(self)
                        break
                    elif winner == match.player2.first_name:
                        self.end_match(match, match.player2)
                        self.player_controller.update_score(self)
                        break
                    else:
                        print("Nom de joueur invalide. Veuillez réessayer")
                else:
                    print("Veuillez saisir un nom de joueur ou 'egalite' pour un match nul, ou 'back' pour revenir en arrière")

        print("Les résultats du round ont été enregistrés avec succès")



    """ fonction pour passer au round suivant """
    def next_round(self):
        round_number = self.current_round_number
        if self.check_round_completion(round_number):
            print("L65 RC Les matchs du round en cours ont été joués")
            next_round_number = round_number + 1  
            self.start_round(next_round_number)
        else:
            print("l69 rc Les matchs du round en cours n'ont pas encore été joués")

    """ fonction pour verifier si tous les matchs du round ont été joué """
    def check_round_completion(self):
        if len(self.matches) == 4:
            for match in self.matches:
                if match.winner is None:
                    return False
            return True
        return False
    
    """ fonction pour démarrer un tournois"""
    def start_round(self, round_number):
        self.current_round_number = round_number 
        print(f"Round {round_number} - {datetime.now}")
        color_player1 = "white"
        color_player2 = "black"

        match_pairs = self.player_controller.choose_random_players(color_player1, color_player2, round_number)

        matches = self.create_matches(match_pairs, round_number)
        # all_players = self.player_controller.get_players()
        # print("l73 tc all_player")
        # if len(all_players) < 8:
        #     print("Il n'y a pas assez de joueurs pour commencer un tour")
        #     return
        # # Choisissez 8 joueurs aléatoires pour le round
        # round_players = random.sample(all_players, 8)
        # random.shuffle(round_players)
        # Creation des matchs du round
        # matches = self.create_matches(round_players, round_number)
        # Afficher les paires de joueurs
        self.display_matches(matches)

    """ fonction pour afficher les joueurs des matchs"""
    def display_matches(self, matches):
        for e, match in enumerate(matches, start=1):
            print(f"Match {e}: {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}")


    """ fonction pour creer les matchs pour 1 round  """
    def create_matches(self, round_players, round_number):
        matches =[]
        for i in range(0, len(round_players) - 1, 2):
        # Vérifiez si l'index suivant dépasse la limite de la liste
            if i + 1 < len(round_players):
                match = self.add_match(round_players[i], round_players[i + 1], "white", "black", round_number)
                matches.append(match)
        return matches


    """ fonction pour verifier que tout les round ont été fait """
    def check_round_complete(self, round_number):
        print(" l133 rc verif round complet", round_number)
        if len(self.matches) == 4:
            for match in self.matches:
                if match.round_number == round_number and match.winner is None:
                    return False
            return True
        return False
    
    
    
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