
""" Information sur le joueur """
class Player:
    def __init__(self, fisrt_name, last_name, birthday, score, rank ):
        self.first_name = fisrt_name
        self.last_name = last_name
        self.birthday = birthday
        self.score = score
        self.rank = rank

#     def view_player(self):
#         print(f"Player {self.first_name} {self.last_name} Date naissance:{self.birthday} Score:{self.score} Rang:{self.rank}")
        
    

# player1 = Player("Pouet Pouet", "Camembert", "16/06/2000", 51, 3)
# player1.view_player()
# print()
# print(player1)
# print()