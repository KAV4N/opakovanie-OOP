from Character import  Character


class Hobbit(Character):
    def __init__(self, name):
        super().__init__(name, race="Hobbit", hp=80)
        self.is_sneaking = False


    def sneak(self):
        if not self.is_sneaking:
            self.is_sneaking = True
            print(f"{self.name} starts sneaking quietly.")
        else:
            print(f"{self.name} is already sneaking.")

    def stop_sneaking(self):
        if self.is_sneaking:
            self.is_sneaking = False
            print(f"{self.name} stops sneaking.")
        else:
            print(f"{self.name} is not currently sneaking.")

    def __str__(self):
        return super().__str__() + " (Ring Bearer)" if self.ring else super().__str__()
