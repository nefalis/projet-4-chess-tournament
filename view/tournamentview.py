from controller.playercontroller import PlayerController
from rich import print
from datetime import datetime


class TournamentView:
    def __init__(self):
        self.player_controller = PlayerController()

    def display_menu_tournament(tournament_controller):
        """ Display the tournament menu options. """
        print("\n[cyan]-- Menu tournoi --[/cyan]\n")
        print("1. Ajouter un tournoi")
        print("2. Voir la liste des tournois")
        print("3. Commencer un tournoi")
        print("4. Reprendre un tournoi")
        print("5. Supprimer un tournoi")
        print("6. Quitter le menu tournoi")

    def create_tournament_input(tournament_controller, player_controller):
        """ Function to create a tournament with user input. """
        name_tournament = input("Entrez le nom du tournoi : ")
        town_tournament = input("Entrez le nom de la ville : ")

    # Prompt for start date and validate
        while True:
            date_start = input("Entrez la date de début du tournoi (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(date_start, "%d/%m/%Y")
                break
            except ValueError:
                print("Format de date incorrect. Veuillez entrer une date au format JJ/MM/AAAA.")

        # Prompt for end date and validate
        while True:
            date_finish = input("Entrez la date de fin du tournoi (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(date_finish, "%d/%m/%Y")
                # Check if end date is after start date
                if datetime.strptime(date_finish, "%d/%m/%Y") > datetime.strptime(date_start, "%d/%m/%Y"):
                    break
                else:
                    print("La date de fin doit être après la date de début.")
            except ValueError:
                print("Format de date incorrect. Veuillez entrer une date au format JJ/MM/AAAA.")

        description_tournament = input("Entrez une description du tournoi du tournoi : ")

        # Ensure number of players is even and greater than 0
        while True:
            number_player = input("Entrez le nombre de joueurs qui participe : ")
            try:
                number_player = int(number_player)
                if number_player > 0 and number_player % 2 == 0:
                    break
                else:
                    print("Le nombre de joueurs doit être pair. Veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        # Create tournament
        rounds_info = {}
        tournament_controller.create_tournament(name_tournament,
                                                town_tournament,
                                                date_start,
                                                date_finish,
                                                number_player,
                                                description_tournament,
                                                rounds_info)

        # Display available players.
        print("Liste des joueurs disponibles :")
        players = player_controller.get_players()
        for index, player in enumerate(players, start=1):
            print(f"{index} prenom : {player.first_name} - nom : {player.last_name} score : {player.score}")

        # Add players to the tournament.
        num_players = int(number_player)
        selected_players = []
        for _ in range(num_players):
            while True:
                try:
                    player_index = int(input("Entrez le numéro du joueur à ajouter au tournoi : "))
                    if 1 <= player_index <= len(players):
                        selected_players.append(players[player_index - 1])
                        break
                    else:
                        print("Veuillez entrer un numéro de joueur valide.")
                except ValueError:
                    print("Veuillez entrer un numéro de joueur valide.")

        tournament_controller.add_player_tournament(selected_players)
        tournament_controller.update_tournament_json("tournamentDB.json")
        print("Le tournoi a été créé avec succès et les joueurs ont été ajouté")

    def select_tournament(tournament_controller):
        """ Function to select a tournament. """
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")
        while True:
            name = input("Entrez le nom du tournoi  : ")
            date = input("Entrez la date du tournoi (format JJ/MM/AAAA) : ")
            for tournament in tournament_controller.tournaments:
                if tournament.name_tournament == name and tournament.date_start == date:
                    return tournament
            print("Aucun tournoi trouvé avec le nom et la date spécifiés. Veuillez réessayer")

    def delete_tournament(tournament_controller):
        """ Function for remove a tournament. """
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")
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
