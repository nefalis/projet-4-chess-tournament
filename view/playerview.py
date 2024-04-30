
from rich import print


class PlayerView:
    """ fonction pour creer le menu joueur"""
    def display_menu_player(player_controller):
        print("\n [cyan]-- Menu Joueur -- [/cyan]\n")
        print("1. Créer un joueur")
        print("2. Afficher tous les joueurs")
        print("3. Supprimer un joueur")
        print("4. Quitter le menu joueur")

    """ fonction pour les input de creation de joueur"""
    def create_player_input(player_controller):
        national_chess_id = input("Entrez l'identifiant national d’échecs : ")
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        birthday = input("Entrez la date de naissance du joueur : ")
        score = input("Entrez le score du joueur : ")
        player_controller.create_player(national_chess_id, first_name, last_name, birthday, score)
        print("Le joueur a été créé avec succès")

    """ fonction pour supprimer un joueur"""
    def delete_players(player_controller):
        print("Liste des joueurs :")
        for player in player_controller.players:
            print(f"{player.first_name} {player.last_name}")
        print("Veuillez renseigner le prénom et nom du joueur a supprimer")
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        player = player_controller.get_player_by_name(first_name, last_name)
        if player:
            player_controller.remove_player(player)
            print(f"{first_name} {last_name} a été supprimé")
        else:
            print("Le joueur spécifié n'existe pas")
