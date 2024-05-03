from rich import print


class ReportView:

    def display_menu_report(report_controller):
        """ Display the report menu options. """
        print("\n[cyan]-- Menu rapport --[/cyan]\n")
        print("1. Liste des joueurs")
        print("2. Liste des tournois")
        print("3. Info et date d'un tournoi")
        print("4. Liste des joueurs d'un tournoi")
        print("5. Rapport d'un tournoi")
        print("6. Quitter le menu rapport")

    def print_controller_report(option):
        match option:
            case 0:
                print("\nAucun tournoi n'est disponible pour affichage.\n")
            case 1:
                print("\nAucun tournoi sélectionné\n")
            case 2:
                print("\nAucun joueur trouvé pour ce tournoi.\n")
            case _:
                print("Bad option")

    def print_controller_report_param(param, option):
        match option:
            case 0:
                print(param)
            case 1:
                print(f"\n Le gagnant du tournoi est : "
                      f"[cyan]{param['first_name']} {param['last_name']} [/cyan] "
                      f"avec un score de {param['score']}\n")
            case _:
                print("Bad option")
