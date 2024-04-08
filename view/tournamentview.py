from controller.playercontroller import PlayerController
class TournamentView:
    def __init__(self):
        self.player_controller = PlayerController()

    """ fonction pour creer le menu tournoi """
    def display_menu_tournament(tournament_controller):
        print("Menu tournoi\n")
        print("1. Ajouter une tournoi")
        print("2. Voir la liste des tournois")
        print("3. Commencer un tournoi")
        print("4. Supprimer un tournoi")
        print("5. Quitter le menu tournoi")

    """ fonction pour les input de creation de tournoi """
    def create_tournament_input(tournament_controller, player_controller):
        name_tournament = input("Entrez le nom du tournoi : ")
        town_tournament = input("Entrez le nom de la ville : ")
        date_start = input("Entrez la date de début du tournoi : ")
        date_finish = input("Entrez la date de fin du tournoi : ")
        number_player = input("Entrez le nombre de joueur qui participe : ")
        description_tournament = input("Entrez une description du tournoi du tournoi : ")

        tournament_controller.create_tournament(name_tournament, town_tournament, date_start, date_finish, number_player, description_tournament, description_tournament)

        # Affichage des joueurs disponibles
        print("Liste des joueurs disponibles :")
        players = player_controller.get_players()
        for index, player in enumerate(players, start=1):
            print(f"{index} prenom : {player.first_name} nom : {player.last_name} score : {player.score}")

        # ajout des joueurs pour le tournoi
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

    """ fonction pour selectionner un tournoi """
    def select_tournament(tournament_controller):
        print("Liste des tournois : ")
        for tournament in tournament_controller.tournaments:
            print(f"{tournament.name_tournament} {tournament.date_start}")
        while True:
            name = input("Entrez le nom du tournoi (ou tapez 'q' pour quitter) : ")
            if name.lower() == 'q':
                return None
            date = input("Entrez la date du tournoi (format JJ/MM/AAAA) : ")
            for tournament in tournament_controller.tournaments:
                if tournament.name_tournament == name and tournament.date_start == date:
                    return tournament
            print("Aucun tournoi trouvé avec le nom et la date spécifiés. Veuillez réessayer")

    """ fonction pour supprimer un tournoi"""
    def delete_tournament(tournament_controller):
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