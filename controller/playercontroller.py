
from models.player import Player

""" fonction pour creer un joueur"""
class PlayerController:

    def __init__(self):
        self.players = []

    def create_player(self, first_name, last_name, birthday, score, rank):
        # Créez une instance de Player en utilisant les arguments fournis
        player = Player(first_name, last_name, birthday, score, rank)
        return player 

# creation d'une instance PlayerController
controller = PlayerController()

# Utilisation de la méthode create_player pour créer un joueur
player = controller.create_player("Pouet Pouet", "Camembert", "16/06/2000", 51, 3)

# Visualisation
print()
print(player)
print()