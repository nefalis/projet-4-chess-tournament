from controller.playercontroller import PlayerController
from controller.tournamentcontroller import TournamentController
from controller.reportcontrolle import ReportController
from view.playerview import PlayerView
from view.tournamentview import TournamentView
from view.reportview import ReportView


def main_player_view():
    player_controller = PlayerController()
    player_controller.create_player_json("./data/playersDB.json")

    while True:
        PlayerView.display_menu_player(player_controller)
        choice = input("\n Choisissez une option : ")

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
        choice = input("\n Choisissez une option : ")

        if choice == '1':
            TournamentView.create_tournament_input(tournament_controller, player_controller)
        elif choice == '2':
            TournamentController.display_tournament(tournament_controller)
        elif choice == '3':
            tournament_controller.start_tournament()
        elif choice == '4':
            tournament_controller.resume_tournament()   
        elif choice == '5':
            TournamentView.delete_tournament(tournament_controller)
        elif choice == '6':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")


def main_report_view():
    tournament_controller = TournamentController()
    tournament_controller.create_tournament_json("tournamentDB.json")
    report_controller = ReportController(tournament_controller)

    while True:
        ReportView.display_menu_report(report_controller)
        choice = input(" Choisissez une option : ")

        if choice == '1':
            report_controller.display_all_player()
        elif choice == '2':
            report_controller.display_all_tournament()
        elif choice == '3':
            report_controller.display_tournament_date_report()
        elif choice == '4':
            report_controller.display_tournament_player_report()
        elif choice == '5':
            report_controller.display_tournament_report()
        elif choice == '6':
            print("Retour au menu principal\n")
            break
        else:
            print("Option invalide. Veuillez réessayer")
