
"""
Interface destinée à la gestion des joueurs
"""
class PlayerView:

    def first_name_player(self):
        first_name_player = input("Prénom du joueur: ")
        return first_name_player
    
    def last_name_player(self):
        last_name_player = input("Nom de famille du joueur: ")
        return last_name_player
    
    def birthday_player(self):
        birthday_player = input("Date de naissance (format DD/MM/YYYY): ")
        return birthday_player
    
    def score_player(self):
        score_player = input("Score du joueur: ")
        return score_player
