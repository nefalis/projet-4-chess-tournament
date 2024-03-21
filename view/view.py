""" 
Menu navigation

1 menu joueur
    1-1 ajout joueur
    1-2 voir la liste de joueur
    1-3 supprimer un joueur
    1-4 quitter le menu joueur
2 menu tournoi
    2-1 ajout tournoi
    2-2 voir la liste des tournois sauvegarder
    2-3 supprimer tournoi
    2-4 quitter le menu tournoi
3 commencer un tournois
    3-1 commencer le 1er round
        3-1-1 entrer résultat 1er round
    3-2 commencer le 2eme round
        3-2-1 entrer résultat 2eme round
    3-3 commencer le 3eme round
        3-3-1 entrer résultat 3eme round
    3-4 commencer le 4eme round
        3-4-1 entrer résultat 4eme round
    3-5 fin du tournoi
    3-6 quitter le menu du tournoi en cours
5 voir les résultats
    5-1 resultat joueur
    5-2 resultat tournoi
6 sortir un rapport 


"""
from controller.playercontroller import PlayerController
from controller.tournamentcontroller import TournamentController
from view.playerview import PlayerView
from view.tournamentview import TournamentView
from view.roundview import RoundView

def main_player_view():
    # création d'une intance player_controller
    player_controller = PlayerController()
    player_controller.create_player_json("playersDB.json")

    while True:
        PlayerView.display_menu_player(player_controller)
        choice = input("Choisissez une option : ")

        if choice == '1':
            PlayerView.create_player_input(player_controller)
        elif choice == '2':
            PlayerView.display_players(player_controller)
        elif choice == '3':
            PlayerView.delete_players(player_controller)
        elif choice == '4':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")

def main_tournament_view():
    # création d'une intance
    tournament_controller = TournamentController()
    tournament_controller.create_tournament_json("tournamentDB.json")

    while True:
        TournamentView.display_menu_tournament(tournament_controller)
        choice = input("Choisissez une option : ")

        if choice == '1':
            TournamentView.create_tournament_input(tournament_controller)
        elif choice == '2':
            TournamentView.display_tournament(tournament_controller)
        elif choice == '3':
            main_round_view(tournament_controller) 
        elif choice == '4':
            TournamentView.delete_tournament(tournament_controller)
        elif choice == '5':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")

def main_round_view(tournament_controller):
    # tournament_controller = TournamentController()
    round_view = RoundView(tournament_controller)


    while True:
        RoundView.display_menu_round_tournament()
        choice = input("Choisissez une option : ")

        if choice == '1':
            round_view.start_tournament_round()
        elif choice == '2':
            round_view.start_first_round()
        elif choice == '3':
            round_view.next_round()
        elif choice == '4':
            tournament_controller.end_tournament()
        elif choice == '5':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")