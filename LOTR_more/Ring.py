class Ring:
    def __init__(self, name):
        self.name = name
        self.holder = None

    def pick_up(self, entity):
        if not self.holder:
            self.holder = entity
            print(f"{entity.name} picks up the {self.name}.")
        else:
            print(f"The {self.name} is already held by {self.holder.name}.")

    def drop(self):
        if self.holder:
            print(f"{self.holder.name} drops the {self.name}.")
            self.holder = None
        else:
            print(f"The {self.name} is not held by anyone.")

    def __str__(self):
        return f"The One Ring ({self.name})"