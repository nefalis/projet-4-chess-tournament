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

    def print_controller_round(option):
        match option:
            case 0:
                print("\nTournoi interrompu par l'utilisateur.\n")
            case 1:
                print("\nVeuillez répondre par 'o' pour oui ou 'n' pour non.\n")
            case 2:
                return input("Voulez-vous continuer oui/non (o/n) ? ").strip().lower()
            case 3:
                print("\nNuméro du joueur invalide. Veuillez réessayer \n")
            case 4:
                print("\nVeuillez saisir un numero de joueur ou 'egalite' pour un match nul, "
                      "'back' pour revenir en arrière\n")
            case 5:
                print("\nLes résultats du round ont été enregistrés avec succès\n")
            case 6:
                print("Le nombre de joueurs doit être pair pour former des paires pour les matchs")

    def print_controller_tournament(option):
        match option:
            case 0:
                print("\nLe fichier n'a pas été trouvé\n")
            case 1:
                print("\nErreur lors du décodage du fichier JSON \n")
            case 2:
                print("\nAucun tournoi en cours \n")
            case 3:
                print("\nAucun tournoi sélectionné\n")
            case 4:
                print("\nErreur: player_data n'est pas un dictionnaire.\n")
            case 5:
                print("\nListe des tournois : \n")
            case 6:
                print("\n[green]Classement des joueurs:[/green]\n")
            case 7:
                print("\nAucun joueur n'a participé au tournoi ou n'a marqué de points.\n")
            case 8:
                print("\nLe tournoi ne peut pas être terminé car tous les rounds n'ont pas été joués\n")
            case 9:
                print("\nLe tournoi a été supprimé\n")
            case 10:
                print("\nLe tournoi spécifié n'existe pas dans la liste des tournois\n")
            case 11:
                print("\nLe tournoi est déjà terminé.\n")
            case 12:
                return input("Entrez le nom du tournoi que vous souhaitez reprendre : ")
            case 13:
                return input("Entrez la date de début du tournoi que vous souhaitez reprendre (format JJ/MM/AAAA) : ")

    def print_controller_tournament_param(param, option):
        match option:
            case 0:
                print(f"\nHeure du début: {param}\n")
            case 1:
                print(f"{param[0].name_tournament} {param[0].date_start}")
            case 2:
                print(f"{param[0]}. {param[1]} - Score: {param[2]} points")
            case 3:
                print(f"\n[yellow]Le vainqueur du tournoi est : {param[0]} avec un score de "
                      f"{param[1]} points[/yellow]")
            case 4:
                print(f"Reprise du tournoi au round {param}.")
            case 5:
                print(f"\n[blue] Vous allez commencer le tournoi {param.name_tournament}[/blue]\n")
            case 6:
                print(f"\n[green]Résultats du Round {param}: [/green]\n")
            case 7:
                print(f"\n[green] Enregistrement des résultats du round {param} :[/green]")
            case 8:
                return input(f"Match {param}, Entrez numéro du vainqueur 1 ou 2, 'egalite' pour match nul, "
                             f"ou 'back' revenir en arrière) : ")
            case 9:
                print(f"\n[blue] Fin du round {param[0]} - {param[1]} [/blue]\n ")
            case 10:
                print(f"{param[0].player1['first_name']} {param[0].player1['last_name']} "
                      f"vs {param[0].player2['first_name']} {param[0].player2['last_name']}: "
                      f"{param[1]}")
            case 11:
                print(f"{param[0]}. {param[1]["first_name"]} {param[1]["last_name"]}")
            case 12:
                print(f"Match {param[0]}: "
                      f"{param[1].player1['first_name']} {param[1].player1['last_name']} "
                      f"vs "
                      f"{param[1].player2['first_name']} {param[1].player2['last_name']}")
