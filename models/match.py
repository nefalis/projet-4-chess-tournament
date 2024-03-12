from datetime import datetime

""" Information sur les matchs """

class Match:
    def __init__(self, player1,player2, color_player1, color_player2):
        self.player1 = player1
        self.player2 = player2
        self.color_player1 = color_player1
        self.color_player2 = color_player2
        self.start_time = None
        self.end_time = None
        self.winner = None
        
    def start_match(self):
        self.start_time = datetime.now()

    def end_match(self, winner):
        self.end_time = datetime.now()
        self.winner = winner