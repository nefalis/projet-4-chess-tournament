from view.view import main_player_view
from view.view import main_tournament_view
from view.view import main_report_view
from rich import print


def main_menu():
    """ Function to display the main menu and handle user navigation. """

    while True:
        print('\n[cyan]-- Menu navigation -- [/cyan]\n')
        print("1. Menu joueur")
        print("2. Menu tournoi")
        print("3. Menu rapport")

        choice = input("Choisissez une option : ")
        if choice == '1':
            main_player_view()
        elif choice == '2':
            main_tournament_view()
        elif choice == '3':
            main_report_view()
        elif choice == '4':
            print("Au revoir")
            break
        else:
            print("Option invalide. Veuillez réessayer")


if __name__ == "__main__":
    main_menu()
