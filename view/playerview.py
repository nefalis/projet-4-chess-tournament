
from rich import print


class PlayerView:

    def display_menu_player(player_controller):
        """ Function to display the player menu and handle user interactions. """
        print("\n [cyan]-- Menu Joueur -- [/cyan]\n")
        print("1. Créer un joueur")
        print("2. Afficher tous les joueurs")
        print("3. Supprimer un joueur")
        print("4. Quitter le menu joueur")

    def create_player_input(player_controller):
        """ Function to handle input for creating a new player and add it to the player controller. """
        national_chess_id = input("Entrez l'identifiant national d’échecs : ")
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        birthday = input("Entrez la date de naissance du joueur : ")
        score = input("Entrez le score du joueur : ")
        player_controller.create_player(national_chess_id, first_name, last_name, birthday, score)
        print("Le joueur a été créé avec succès")

    def delete_players(player_controller):
        """ Function for remove a player """
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

    def display_players(self):
        """ Display the list of players. """
        print("\n[cyan] Liste des joueurs :[/cyan]\n")
        for player in self.players:
            print(f"{player.first_name} {player.last_name}")

    def print_controller_player(option):
        match option:
            case 0:
                print("\n Le joueur a été supprimé. \n")
            case 1:
                print("\n Le joueur spécifié n'existe pas dans la liste des joueurs. \n")
            case 2:
                print("\n Le fichier n'a pas été trouvé \n")
            case 3:
                print("\n Erreur lors du décodage du fichier JSON \n")
            case 4:
                print("\n Liste des joueurs : \n")
            case _:
                print("Bad option")
