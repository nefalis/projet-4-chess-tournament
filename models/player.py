
""" Information sur le joueur """
class Player:
    def __init__(self, first_name, last_name, birthday, score ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.score = score

    def update_score(self, points):
        self.score += points

