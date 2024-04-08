
""" Information sur le tournois """
class Tournament:
    def __init__(self, name_tournament, town_tournament, date_start, date_finish, number_round, number_player, description_tournament, players ):
        self.name_tournament = name_tournament
        self.town_tournament = town_tournament
        self.date_start = date_start
        self.date_finish = date_finish
        self.number_round = number_round
        self.number_player = number_player
        self.description_tournament = description_tournament
        self.players = players

    def add_player(self, player):
        player_dict = dict(
            first_name = player.first_name,     
            last_name = player.last_name,
            score = player.score)
        self.players.append(player_dict)

    def end_tournament(self, end_time):
        self.date_finish = end_time