

class Soldier:

    def __init__(self, soldier_id, first_name, last_name, phon_number, rank):
        self.soldier_id = soldier_id
        self.first_name = first_name
        self.last_name = last_name
        self.phon_number = phon_number
        self.rank = rank


    def __repr__(self):
        return f"Soldier({self.soldier_id}, {self.first_name}, {self.last_name}, {self.rank})"
    
    def __str__(self):
        return f"Soldier ID: {self.soldier_id}, Name: {self.first_name} {self.last_name}, Rank: {self.rank}"