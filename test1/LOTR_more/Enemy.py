from Character import  Character

class Enemy(Character):
    def __init__(self, name, species, damage=25):
        super().__init__(name, race=species, hp=100)
        self.damage = damage

    def attack(self, target):
        if target.is_alive():
            target.take_damage(self.damage)
            print(f"{self.name} attacks {target.name} with ferocity! Damage: {self.damage}")
        else:
            print(f"{self.name} cannot attack {target.name}, they are already defeated.")

    def check_damage_status(self):
        print(f"{self.name}'s current damage: {self.damage}")

    def grunt(self):
        print(f"{self.name} lets out a menacing grunt.")

    def __str__(self):
        return super().__str__() + f" (Damage: {self.damage})"
