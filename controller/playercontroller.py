"""
C create
R read
U uptdate
D delete
"""

import json
import os
import random

from models.player import Player

""" fonction pour creer un joueur"""
class PlayerController:

    def __init__(self):
        self.players = []

    """ fonction pour la création d'un joueur"""
    def create_player(self, first_name, last_name, birthday, score):
        # Créez une instance de Player en utilisant les arguments fournis
        player = Player(first_name, last_name, birthday, score)
        self.players.append(player)
        print("les joueurs sont crée")
        return player 
    
    """ fonction pour creer un fichier json"""
    def create_player_json(self, filename):
        data_folder = "data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        full_path = os.path.join(data_folder, filename)
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                players_data = json.load(f)
                self.players = [Player(**player_data) for player_data in players_data] 
            
    """ fonction pour mettre a jour le fichier json """
    def update_player_json(self, filename):
        data_folder = "data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        full_path = os.path.join(data_folder, filename)
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump([player.__dict__ for player in self.players], json_file, indent=4, ensure_ascii=False)
        
    """ pour mettre a jour les rangs"""
    def update_score(self, match_controller):
        # Réinitialiser le score de tous les joueurs à 0
        for player in self.players:
            player.score = 0
        # Parcourir tous les matchs
        for match in match_controller.matches:
            # Si un vainqueur est déclaré
            if match.winner:
                # Incrémenter le score du vainqueur de ce match
                match.winner.score += 1
                print("je rajoute 1 au vainqueur")

    """ fonction pour choisir des joueurs aléatoire"""
    def choose_random_players(self, list_players, test):
        print(len(self.players))
        print("ligne64 playercontrol")
        print(list_players)
        print(type(len(self.players)))
        # if list_players > len(self.players qui devient test et get au final):
        #     print("Il n'y a pas assez de joueurs disponible.")
        #     return []
        random_players = random.sample(test, list_players)
        print("pik nik douille c'est toi l'andouille")
        return random_players

    """ pour mettre a jour les points"""
    def update_points(self, player, points):
        player.score += points

    """ pour rechercher un joueur specifique afin de modifier des informations"""
    def get_player_by_name(self, first_name, last_name):
        for player in self.players:
            if player.first_name == first_name and player.last_name == last_name:
                return player
            return None

    """ fonction pour enlever un joueur"""
    def remove_player(self, player):
        if player in self.players:
            print(f"Le joueur {player.first_name} {player.last_name} a été supprimé.")
        else:
            print("Le joueur spécifié n'existe pas dans la liste des joueurs.")

# Créez une instance de PlayerController
controller = PlayerController()

# # liste de joueur
# controller.create_player("Pouet Pouet", "Camembert", "16/06/2000", 1),
# controller.create_player("Nuut", "Ella", "05/06/2000", 1),
# controller.create_player("Remi", "Fasol", "14/10/2000", 1),
# controller.create_player("Tim", "Faitchier", "03/02/2001", 1),
# controller.create_player("Harry", "Cover", "29/05/2001", 1),
# controller.create_player("Emma", "Carena", "29/04/2001", 1),
# controller.create_player("Laura", "Tatouille", "04/04/2000", 1),
# controller.create_player("Claire", "Voyance", "12/08/2000", 1)



    
    # """ fonction pour sauvegarder les joueurs
    #     methode dump enregistre les données json
    # """
    # def save_players_to_json(self, filename):
    #     with open(filename, 'w') as f:
    #         json.dump([player.__dict__ for player in self.players], f)

    
    # """ fonction pour charger des joueurs"""
    # def load_players_from_json(self, filename):
    #     with open(filename, 'r') as f:
    #         players_data = json.load(f)
    #         self.players = [Player(**player_data) for player_data in players_data]