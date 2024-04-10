from rich.table import Table
from rich import print


class ReportView:
   
    """ fonction pour creer le menu rapport """
    def display_menu_report(report_controller):
        print(f"\n[cyan]-- Menu rapport --[/cyan]\n")
        print("1. Liste des joueurs")
        print("2. Liste des tournois")
        print("3. Rapport d'un tournoi")
        print("4. Liste des joueurs d'un tournoi")
        print("5. Quitter le menu rapport")

        

    