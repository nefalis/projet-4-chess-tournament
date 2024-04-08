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
        self.selected_players = []
        self.load_players("./data/playersDB.json")
        self.player_id_counter = 1

    """ fonction pour la création d'un joueur"""
    def create_player(self, national_chess_id, first_name, last_name, birthday, score):
        player = Player(national_chess_id, first_name, last_name, birthday, score)
        self.players.append(player)
        self.update_player_json("playersDB.json")
        print("Le joueur a été crée")
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

    """ fonction pour charger les joueurs"""
    def load_players(self, filename):
        try:
            with open(filename, 'r') as file:
                players_data = json.load(file)
                self.players = [Player(player_data["national_chess_id"], player_data["first_name"], player_data["last_name"], player_data["birthday"], int(player_data["score"])) for player_data in players_data]
        except FileNotFoundError:
            print(f"Le fichier {filename} n'a pas été trouvé")
        except json.JSONDecodeError:
            print(f"Erreur lors du décodage du fichier JSON {filename}")

    """ fonction pour avoir les joueurs"""
    def get_players(self):
        print("l62 pc get player")
        return self.players

    

   
    
    """ fonction pour afficher la liste des joueurs"""
    def display_players(self):
        print("Liste des joueurs :")
        for player in self.players:
            print(f"{player.first_name} {player.last_name}")          

    # """ pour mettre a jour les points"""
    # def update_points(self, player, points):
    #     player.score += points
    #     print("l77 player control - up point")

    """ pour rechercher un joueur specifique afin de modifier des informations"""
    def get_player_by_name(self, first_name, last_name):
        for player in self.players:
            if player.first_name == first_name and player.last_name == last_name:
                return player
        return None
    
    
    """ fonction pour enlever un joueur"""
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            self.update_player_json("playersDB.json")
            print(f"Le joueur {player.first_name} {player.last_name} a été supprimé.")
        else:
            print("Le joueur spécifié n'existe pas dans la liste des joueurs")


""" fonction pour choisir des joueurs aléatoire)
    def choose_random_players(self):
        print("ligne64 playercontrol")
        print(list_players)
        # if list_players > len(self.players qui devient test et get au final):
        #     print("Il n'y a pas assez de joueurs disponible.")
        #     return []
        population = self.players
        if list_players > len(population):
            print("Le nombre de joueurs à sélectionner est supérieur au nombre de joueurs disponibles")
        if len(self.players) % 2 != 0:
            print("Le nombre de joueurs doit être pair pour former des paires pour les matchs")
            return []
        random_players = random.sample(population, list_players)
        random_players = random.sample(self.players, len(self.players))
        print("l71 playcontrol - pik nik douille c'est toi l'andouille")
        return random_players """


# # liste de joueur
# controller.create_player("Pouet Pouet", "Camembert", "16/06/2000", 1),
# controller.create_player("Nuut", "Ella", "05/06/2000", 1),
# controller.create_player("Remi", "Fasol", "14/10/2000", 1),
# controller.create_player("Tim", "Faitchier", "03/02/2001", 1),
# controller.create_player("Harry", "Cover", "29/05/2001", 1),
# controller.create_player("Emma", "Carena", "29/04/2001", 1),
# controller.create_player("Laura", "Tatouille", "04/04/2000", 1),
# controller.create_player("Claire", "Voyance", "12/08/2000", 1)