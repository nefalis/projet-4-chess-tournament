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
        
        player1['played_with'].append(player2['national_chess_id'])
        player2['played_with'].append(player1['national_chess_id'])

        return match


    """ fonction pour afficher les resultats apres chaque round"""
    def display_round_results(self, round_number):
        print(f"\n[green]Résultats du Round {round_number}: [/]\n")
        round_matches = [match for match in self.matches if match.round_number == round_number]
        for match in round_matches:
            if match.winner is not None :
                winner_name = f"{match.winner['first_name']} {match.winner["last_name"]}"
            else:
                winner_name = "Égalité"

            print(f"{match.player1['first_name']} {match.player1['last_name']} vs {match.player2['first_name']} {match.player2['last_name']}: {winner_name}")



    def end_match(self, match, winner):
        match.winner = winner
        if winner:
            print(f"j'ajoute 1 au gagnant {winner}")
            winner["score"] += 1  
            # Déterminez le perdant et mettez à jour son score à 0
            loser = match.player1 if winner != match.player1 else match.player2
            print(f"j'ajoute 0 au perdant {loser}")
            # loser["score"] = 0
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
        print("round info l 100 rc")
        print(self.tournament_controller.round_info)
    
    """ fonction pour démarrer un tournois"""
    def start_round(self, round_number):
        self.current_round_number = round_number 
        start_time = datetime.now()
        print(f"[blue]\n Round {round_number} - {start_time} [/blue]\n")
        
        # je recupere les joueurs
        tournament_players = self.tournament_controller.get_tournament_players()

        sorted_players = sorted(tournament_players, key=lambda x: x["score"], reverse=True)
        if round_number > 1:
            selected_players = sorted_players
        else :
            selected_players = random.sample(sorted_players, len(tournament_players))

        matches = []
        matches = self.create_matches(selected_players, round_number)
        self.display_matches(matches)
        self.record_match_results(round_number, matches)
        self.get_match_result(matches)

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

        for i in range(0, len(players)):
            players[i]['selected'] = False

        for i in range(0, len(players) ):
            print(f" {i} tour de boucle *--*---*------*-------*******----*--***-")
            if players[i]['selected']:
                print(f" l 174 - joueur deja en match {players[i]['first_name']} ")
                continue
            else:
                print(f"l 177 - joueur libre {players[i]['first_name']} devient player1 {players[i]['national_chess_id']}")
                player1 = players[i]
                players[i]['selected'] = True
                print(f"\n l 181 avant if - valeur de i : {i} ")
                print(f"l 181 avant if - valeur de i +1 : {i+1} ")
                print(f"l 181 avant if - valeur de ilen(players) : {len(players)} \n")

                if i+1 < len(players):
                    print(f"l 181 - i+1 est possible {players[i+1]['first_name']}")
                    print(f"{players[i+1]['selected']} {players[i+1]['played_with']} l 183")
                    if players[i+1]['selected'] == False and player1['national_chess_id'] not in players[i+1]['played_with']:
                        print(f"  l 183  {players[i+1]['first_name']} est dispo et n'a pas joué contre j1")
                        player2 = players[i+1]
                        players[i+1]['selected'] = True
                        match = self.add_match(player1, player2, "white", "black", round_number)
                        matches.append(match)
                        print(f"match ajouté avec {players[i]['first_name']}, {players[i+1]['first_name']}")
                        continue
                    else:
                        print(f"l 193 joeur pas dispo ou deja jouer contre on y retourne")
                        for k in range(0, len(players)):
                            print(f" {k} l 194 tour de boucle +++++++--+---+++-----++++++- ")
                            print(f"\n{players[i]['first_name']}  - {players[i]['national_chess_id']} - {players[i]['selected']} - {players[i]['played_with']}  l 200 \n")
                            print(f"{players[k]['first_name']}  - {players[k]['national_chess_id']} - {players[k]['selected']} - {players[k]['played_with']}  l 200 \n")

                            if players[k]['selected']  or players[k]['national_chess_id'] == player1['national_chess_id'] or player1['national_chess_id'] in players[k]['played_with']:
                                print(f" l 194 {players[k]['first_name']} est deja en match ou j2=j1 ou j1 deja avec j2")
                                continue
                            else:
                                print(f" l 197 {players[k]['first_name']} devient j2 et c'est parti")
                                player2 = players[k]
                                player2['selected'] = True
                                match = self.add_match(player1, player2, "white", "black", round_number)
                                matches.append(match)
                                break
                else:
                    print(" on est au elseeeeeeeeeeuuuuhhhhhh l 215 ")
                    for k in range(0, len(players)):
                            if players[k]['selected']  or players[k]['national_chess_id'] == player1['national_chess_id'] or player1['national_chess_id'] in players[k]['played_with']:
                                continue
                            else:
                                print(" je suis rentrééééééééé dans le dernier elseeeeuuuhhhh l 219")
                                player2 = players[k]
                                player2['selected'] = True
                                match = self.add_match(player1, player2, "white", "black", round_number)
                                matches.append(match)
                                break
        return matches

        

        #     match_player2 = players[i+1]
        #     # print(f"id du joueur 2 avant if {match_player2['national_chess_id']}")
        #     print(f" valeur de i {i} l 156")
        #     stop = False
        #     j = i+1
        #     # verif si player1 et player 2 ont deja joué ou non ensemble
        #     while not stop:
                
        #         if players[i]['national_chess_id'] not in match_player2['played_with'] and match_player2['national_chess_id'] != players[i]['national_chess_id']:
        #             print(f"while_if l 162")
        #             # Sélection d'un nouveau joueur pour match_player2
        #             if  j < len(players):
        #                 print(" pouet if l 164 while_if_if")
        #                 match_player2 = players[j]
                        
        #             else:
        #                 print("pouet else l 168 while_if_else")
        #                 # Revenir au début de la liste des joueurs
        #                 match_player2 = players[0]

        #             stop =True
        #         if j < len(players):
        #             print(" while_if l176")
        #             j = j+1  
        #         else:
        #             print(" while_else l 179")
        #             j=0

        #         print("l 176 while finiiiiiii")
        
        #     # print(f"l168 juste avant add match {match_player2['national_chess_id']}")
        #     match = self.add_match(players[i], match_player2, "white", "black", round_number)
        #     matches.append(match)
        # return matches
    
    
    def match_exists(self, player1, player2):
        # verif si le match a deja été joué
        for match in self.tournament_controller.current_tournament.matches:
            if (match.player1 == player1 and match.player2 == player2) or (match.player1 == player2 and match.player2 == player1):
                return match 
        return None


    """ fonction pour verifier que tout les round ont été fait """
    def check_round_complete(self, round_number):
        if self.current_round_number >= self.total_rounds:
            return True
        return False
    
        # """ pour mettre a jour les rangs"""
    # def update_score(self, matches):
    #     for match in matches:
    #         self.end_match(match, match.winner)
    #     self.tournament_controller.update_tournament_json("tournamentDB.json")
    #     print("Le score des joueurs a été mis à jour dans le fichier JSON.")

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