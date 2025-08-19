

class Soldier:

    id_number = 0

    def __init__(self, soldier_id, first_name, last_name, rank):
        self.soldier_id = Soldier.id_number + 1
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank


    def __repr__(self):
        return f"Soldier({self.soldier_id}, {self.first_name}, {self.last_name}, {self.rank})"
    
    def __str__(self):
        return f"Soldier ID: {self.soldier_id}, Name: {self.first_name} {self.last_name}, Rank: {self.rank}"