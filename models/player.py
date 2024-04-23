
""" Information sur le joueur """
class Player:
    def __init__(self, national_chess_id, first_name, last_name, birthday, score ):
        self.national_chess_id = national_chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.score = score
        self.played_with = []
        self.selected = False
        


    def update_score(self, points):
        self.score += points

    def add_id(self, id):
        self.id = id

