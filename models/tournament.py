
""" Information sur le tournois """
class Tournament:
    def __init__(self, name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament ):
        self.name_tournament = name_tournament
        self.town_tournament = town_tournament
        self.date_start = date_start
        self.date_finish = date_finish
        self.number_round = number_round
        self.number_player = number_player
        self.description_tournament = description_tournament
        self.players = []

    """rajouter un get player pour donner liste joueur a la place de test"""
    def add_player(self, player):
        self.players.append(player)

    def end_tournament(self, end_time):
        self.date_finish = end_time