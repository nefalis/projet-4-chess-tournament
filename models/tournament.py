

class Tournament:
    def __init__(self, name_tournament, town_tournament, date_start, date_finish,
                 number_round, number_player, description_tournament, players, rounds_info):
        """ Initializes a Tournament object with the given attributes. """
        self.name_tournament = name_tournament
        self.town_tournament = town_tournament
        self.date_start = date_start
        self.date_finish = date_finish
        self.number_round = number_round
        self.number_player = number_player
        self.description_tournament = description_tournament
        self.players = players
        self.rounds_info = rounds_info

    def add_player(self, player):
        """ Adds a player to the tournament. """
        player_dict = dict(
            national_chess_id=player.national_chess_id,
            first_name=player.first_name,
            last_name=player.last_name,
            score=player.score,
            played_with=player.played_with,
            selected=False)
        self.players.append(player_dict)

    def end_tournament(self, end_time):
        """ Ends the tournament and sets the finish date. """
        self.date_finish = end_time
