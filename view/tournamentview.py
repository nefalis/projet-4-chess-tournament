from controller.tournamentcontroller import TournamentController


class TournamentView:
    """ fonction pour creer le menu tournoi """
    def display_menu_tournament(tournament_controller):
        print("Menu tournoi\n")
        print("1. Ajouter une tournoi")
        print("2. Voir la liste des tournois")
        print("3. Supprimer un tournoi")
        print("4. Quitter le menu tournoi")

    """ fonction pour les input de creation de tournoi """
    def create_tournament_input(tournament_controller):
        name_tournament = input("Entrez le nom du tournoi : ")
        town_tournament = input("Entrez le nom de la ville : ")
        date_start = input("Entrez la date de début du tournoi : ")
        date_finish = input("Entrez la date de fin du tournoi : ")
        number_round = input("Entrez le nombre de round du tournoi : ")
        number_player = input("Entrez le nombre de joueur qui participe : ")
        description_tournament = input("Entrez une description du tournoi du tournoi : ")
        tournament_controller.create_tournament(name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament)
        tournament_controller.update_tournament_json("tournamentDB.json")
        print("Le tournoi a été créé avec succès")

    """ fonction pour afficher la liste des tournois """
    def display_tournament(tournament_controller):
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")

    """ fonction pour supprimer un tournoi"""
    def delete_tournament(tournament_controller):
        print("Veuillez renseigner le nom et date du tournoi a supprimer")
        name_tournament = input("Entrez le nom du tournoi : ")
        date_start = input("Entrez la date de début du tournoi : ")
        tournament = tournament_controller.get_tournament_by_name(name_tournament, date_start)
        if tournament:
            tournament_controller.remove_tournament(tournament)
            tournament_controller.update_tournament_json("tournamentDB.json")
            print(f"{name_tournament} {date_start} a été supprimé")
        else:
            print("Le tournoi spécifié n'existe pas")
