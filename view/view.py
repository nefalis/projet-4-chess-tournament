from controller.playercontroller import PlayerController
from controller.tournamentcontroller import TournamentController
from controller.roundcontroller import RoundController
from view.playerview import PlayerView
from view.tournamentview import TournamentView
from view.roundview import RoundView

def main_player_view():
    # création d'une intance player_controller
    player_controller = PlayerController()
    player_controller.create_player_json("./data/playersDB.json")

    while True:
        PlayerView.display_menu_player(player_controller)
        choice = input("Choisissez une option : ")

        if choice == '1':
            PlayerView.create_player_input(player_controller)
        elif choice == '2':
            PlayerController.display_players(player_controller)
        elif choice == '3':
            PlayerView.delete_players(player_controller)
        elif choice == '4':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")

def main_tournament_view():
    tournament_controller = TournamentController()
    tournament_controller.create_tournament_json("tournamentDB.json")
    player_controller = PlayerController()

    while True:
        TournamentView.display_menu_tournament(tournament_controller)
        choice = input("Choisissez une option : ")

        if choice == '1':
            TournamentView.create_tournament_input(tournament_controller, player_controller)
        elif choice == '2':
            TournamentController.display_tournament(tournament_controller)
        elif choice == '3':
            tournament_controller.start_tournament()
        elif choice == '4':
            TournamentView.delete_tournament(tournament_controller)
        elif choice == '5':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")

# def main_round_view(tournament_controller):
#     # tournament_controller = TournamentController()
#     round_controller = RoundController(tournament_controller)


#     while True:
#         RoundView.display_menu_round_tournament()
#         choice = input("Choisissez une option : ")

#         if choice == '1':
#             round_controller.start_tournament_round()
#         elif choice == '2':
#             round_controller.start_first_round()
#         elif choice == '3':
#             round_controller.next_round()
#         elif choice == '4':
#             tournament_controller.end_tournament()
#         elif choice == '5':
#             print("Retour au menu principal\n")
#             break
#         else:
#             print("Option invalide. Veuillez réessayer")