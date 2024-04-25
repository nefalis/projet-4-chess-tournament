from datetime import datetime


class Round:
    def __init__(self, number_round, begin_round, end_round):
        self.number_round = number_round
        self.begin_round = begin_round
        self.end_round = end_round


class Match:
    def __init__(self, player1, player2, color_player1, color_player2, round_number):
        self.player1 = player1
        self.player2 = player2
        self.color_player1 = color_player1
        self.color_player2 = color_player2
        self.start_time = None
        self.end_time = None
        self.winner = None
        self.round_number = round_number

    def start_match(self):
        self.start_time = datetime.now()

    def end_match(self, winner):
        self.end_time = datetime.now()
        self.winner = winner
