import json
import os
from models.player import Player


class PlayerController:

    def __init__(self):
        self.players = []
        self.selected_players = []
        self.load_players("./data/playersDB.json")
        self.player_id_counter = 1

    def create_player(self, national_chess_id, first_name, last_name, birthday, score):
        """ Create a new player and then add to the player database. """
        player = Player(national_chess_id, first_name, last_name, birthday, score)
        self.players.append(player)
        self.update_player_json("playersDB.json")
        print("Le joueur a été crée")
        return player

    def create_player_json(self, filename):
        """ Create player database from a JSON file and populate the player list. """
        # Define the folder where the data will be stored
        data_folder = "data"
        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        # Construct the full path to the JSON file
        full_path = os.path.join(data_folder, filename)
        # Check if the JSON file exists
        if os.path.exists(full_path):
            # If it exists, load the player data from the file
            with open(full_path, 'r') as f:
                players_data = json.load(f)
                self.players = [Player(**player_data) for player_data in players_data]

    def update_player_json(self, filename):
        """ Update player data JSON file with current player information. """
        data_folder = "data"
        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        # Construct the full path to the JSON file
        full_path = os.path.join(data_folder, filename)
        # write player data to the JSON file
        with open(full_path, "w", encoding="utf-8") as json_file:
            # Serialize player objects into dictionnaries and write to the JSON file
            json.dump([player.__dict__ for player in self.players], json_file, indent=4, ensure_ascii=False)

    def load_players(self, filename):
        """ Load player data from a JSON file """
        try:
            # Attempt to open the specified JSON file for reading
            with open(filename, 'r') as file:
                players_data = json.load(file)
                # Extract the player attribute from the data and create Player objects
                self.players = [
                    Player(
                        player_data["national_chess_id"],
                        player_data["first_name"],
                        player_data["last_name"],
                        player_data["birthday"],
                        int(player_data["score"])
                    )
                    for player_data in players_data
                ]
        except FileNotFoundError:
            print(f"Le fichier {filename} n'a pas été trouvé")
        except json.JSONDecodeError:
            print(f"Erreur lors du décodage du fichier JSON {filename}")

    def display_players(self):
        """ Display the list of players. """
        print("\n Liste des joueurs :")
        for player in self.players:
            print(f"{player.first_name} {player.last_name}")

    def get_players(self):
        """ Retrieve the list of players. """
        return self.players

    def get_player_by_name(self, first_name, last_name):
        """ Retrieve a player by their first name and the last name. """
        for player in self.players:
            if player.first_name == first_name and player.last_name == last_name:
                return player
        return None

    def remove_player(self, player):
        """ Remove a player from the list. """
        if player in self.players:
            self.players.remove(player)
            self.update_player_json("playersDB.json")
            print(f"Le joueur {player.first_name} {player.last_name} a été supprimé.")
        else:
            print("Le joueur spécifié n'existe pas dans la liste des joueurs")
