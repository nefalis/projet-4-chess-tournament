
from view.view import main_player_view
from view.view import main_tournament_view

def main_menu():
    while True:
        print("Menu navigation\n")
        print("1. Menu joueur")
        print("2. Menu tournoi")
        print("3. Commencer un tournoi")
        print("4. Voir les résultats")
        print("5. Sortir un rapport")
        print("6. Quitter")

        choice = input("Choisissez une option : ")

        if choice == '1':
            main_player_view()
        elif choice == '2':
            main_tournament_view()
        elif choice == '3':
            start_tournament()
        # elif choice == '4':
        #     view_results()
        # elif choice == '5':
        #     generate_report()
        elif choice == '6':
            print("Au revoir")
            break
        else:
            print("Option invalide. Veuillez réessayer")


if __name__ == "__main__":
    main_menu()

# from controller.playercontroller import PlayerController
# from controller.matchcontroller import MatchController
# from controller.tournamentcontroller import TournamentController
# from datetime import datetime

# # Création des instances
# player_controller = PlayerController()
# tournament_controller = TournamentController()
# match_controller = MatchController()

# # Obtenez l'heure actuelle
# end_time = datetime.now()

# # Créer des joueurs
# player1 = player_controller.create_player("Pouet pouet", "Camembert", "16/06/2000", 0)
# player2 = player_controller.create_player("Nuut", "Ella", "05/06/2000", 0)
# player3 = player_controller.create_player("Remi", "Fasol", "14/10/2000", 0)
# player4 = player_controller.create_player("Tim", "Faitchier", "03/02/2001", 0)
# player5 = player_controller.create_player("Harry", "Cover", "29/05/2001", 0)
# player6 = player_controller.create_player("Emma", "Carena", "29/04/2001", 0)
# player7 = player_controller.create_player("Laura", "Tatouille", "04/04/2000", 0)
# player8 = player_controller.create_player("Claire", "Voyance", "12/08/2000", 0)

# # Créer un tournoi
# new_tournament = tournament_controller.create_tournament("Tournois d'echec", "Le Mans", "2024-03-12", "2024-03-15", 4, 8, "Tournois annuel du Mans")

# # Enregistrer le tournois
# tournament_controller.create_tournament_json("tournamentDB.json")

# # Charger les joueurs depuis le fichier JSON
# player_controller.create_player_json("playersDB.json")

# # Liste de joueurs à ajouter au tournoi
# players_to_add = [player1, player2, player3, player4, player5, player6, player7, player8]

# # Appelez la méthode add_player_tournament
# tournament_controller.add_player_tournament(players_to_add)

# # debut round 
# tournament_controller.start_round()

# # Créer un match entre les joueurs
# match = match_controller.add_match(player1, player2, "white", "black")

# # Démarrer le tournoi
# tournament_controller.start_tournament()

# # Début du match
# match.start_match()
# print("l50 main - start match")

# # Simuler la fin du match avec un vainqueur
# winner = player1  
# match_controller.end_match(match, winner)
# print("l55 main - finish match")

# # Mettre à jour les points du joueur gagnant
# # Ajout de 1 point
# player_controller.update_points(winner, 1) 

# # Ajouter le match au match_controller ?
# match_controller.matches.append(match)

# # Mettre à jour les score des joueurs 
# player_controller.update_score(match_controller)

# # Fin du tournois
# tournament_controller.end_tournament(end_time)

# # Afficher les joueurs triés par score
# sorted_players = sorted(player_controller.players, key=lambda x: x.score, reverse=True)
# for player in sorted_players:
#     print(f"Nom du joueur: {player.first_name} {player.last_name} Score: {player.score}")

# # Enregistrer les joueurs dans un fichier JSON
# player_controller.update_player_json("playersDB.json")

# # Enregistrer le tournois dans un fichier JSON
# tournament_controller.update_tournament_json("tournamentDB.json")

