""" fonction a faire
- modification des points
- supprimer joueur
- ajouter joueur
- modification information
"""

from models.player import Player
import json

""" fonction pour creer un joueur"""
class PlayerController:

    def __init__(self):
        self.players = []

    """ fonction pour la création d'un joueur"""
    def create_player(self, first_name, last_name, birthday, score, rank):
        # Créez une instance de Player en utilisant les arguments fournis
        player = Player(first_name, last_name, birthday, score, rank)
        self.players.append(player)
        return player 
    
    """ fonction pour sauvegarder les joueurs"""
    def save_players_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([player.__dict__ for player in self.players], f)

    """ fonction pour charger des joueurs"""
    def load_players_from_json(self, filename):
        with open(filename, 'r') as f:
            players_data = json.load(f)
            self.players = [Player(**player_data) for player_data in players_data]


    """ fonction pour trier les joueurs par score"""
    def order_player(self, player):
        return player.score

# Créez une instance de PlayerController
controller = PlayerController()

# liste de joueur
controller.create_player("Pouet Pouet", "Camembert", "16/06/2000", 51, 5),
controller.create_player("Nuut", "Ella", "05/06/2000", 22, 8),
controller.create_player("Remi", "Fasol", "14/10/2000", 90, 2),
controller.create_player("Tim", "Faitchier", "03/02/2001", 35, 6),
controller.create_player("Harry", "Cover", "29/05/2001", 84, 3),
controller.create_player("Emma", "Carena", "29/04/2001", 54, 4),
controller.create_player("Laura", "Tatouille", "04/04/2000", 30, 7),
controller.create_player("Claire", "Voyance", "12/08/2000", 97, 1)


# Enregistrez les joueurs dans un fichier JSON
controller.save_players_to_json("playersDB.json")

# Chargez les joueurs à partir du fichier JSON
controller.load_players_from_json("playersDB.json")

# permet de trier les joueurs
controller.players.sort(key=controller.order_player, reverse=True)

# pour afficher le resultat
for player in controller.players:
    print(f"Nom du joueur: {player.first_name} {player.last_name}  Date naissance: {player.birthday} Score: {player.score} Rang: {player.rank}")




# from models.player import Player
# from view.playerview import PlayerView

# """ fonction pour creer un joueur """
# class PlayerController:

#     def __init__(self):
#         self.view = PlayerView()
#         self.players = []

#     def create_player(self):
#         # Créez une instance de Player en utilisant les arguments fournis dans playerview
#         player = Player(
#             self.view.first_name_player,
#             self.view.last_name_player,
#             self.view.birthday_player,
#             self.view.score_player,
#             self.view.rank_player)
#         return player 

# # Créez une instance de PlayerController
# controller = PlayerController()

# # Utilisation de la méthode create_player pour créer un joueur
# player = controller.create_player()

# # Afficher les informations du joueur
# print("Nom complet du joueur:", player.first_name, player.last_name)
# print("Date de naissance du joueur:", player.birthday)
# print("Score du joueur:", player.score)
# print("Rang du joueur:", player.rank)