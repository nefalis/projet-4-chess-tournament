
class RoundView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    """ fonction pour commencer un tournoi """
    def display_menu_round_tournament():
        print("Commencer un tournoi")
        print("1 Commencer le tournoi")
        print("2 Commencer le 1er round")
        print("3 Passer au round suivant")
        print("4 Fin du tournoi")
        print("5 Quitter le menu du tournoi en cours")
