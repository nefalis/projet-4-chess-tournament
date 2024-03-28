
class TournamentView:
    """ fonction pour creer le menu tournoi """
    def display_menu_tournament(tournament_controller):
        print("Menu tournoi\n")
        print("1. Ajouter une tournoi")
        print("2. Voir la liste des tournois")
        print("3. Commencer un tournoi")
        print("4. Supprimer un tournoi")
        print("5. Quitter le menu tournoi")

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

        # ajout des joueurs pour le tournoi
        num_players = int(number_player)
        players = []
        for _ in range(num_players):
            first_name = input("Entrez le prénom du joueur : ")
            last_name = input("Entrez le nom de famille du joueur : ")
            players.append((first_name, last_name))
    
        # Ajout des joueurs au tournoi
        tournament_controller.add_player_tournament(players)
        tournament_controller.update_tournament_json("tournamentDB.json")
        print("Le tournoi a été créé avec succès et les joueurs ont été ajoutés")

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