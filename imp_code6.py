""" More Dunder Methods """

class Club:
    def __init__(self,name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self,i):
        return self.players[i]

    def __repr__(self):
        return f"Club {self.name} : {self.players}"

    def __str__(self):
        return f"{self.name} with {self.players} players"


club_data = Club("LNB club")
club_data.players.append("akash")
club_data.players.append('aman')
print(repr(club_data))
print(str(club_data))
