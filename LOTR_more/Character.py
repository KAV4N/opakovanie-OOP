class Character:
    def __init__(self, name, race, hp=100):
        self.name = name
        self.race = race
        self.hp = hp
        self.is_dead = False
        self.world = None
        self.ring = None

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage. Current HP: {self.hp}")

        if self.hp <= 0:
            self.is_dead = True
            print(f"{self.name} has been defeated!")

            # Remove the character from the world
            if self.world and self in self.world.objects:
                self.world.objects.remove(self)
                print(f"{self.name} has been removed from the world.")

            # Drop the ring if the character is defeated
            if self.ring:
                self.ring.drop()
                self.ring = None

    def is_alive(self):
        return not self.is_dead

    def get_world(self):
        return self.world

    def set_world(self, world):
        self.world = world

    def hold_ring(self, ring):
        if not self.is_dead:
            if self.ring:
                self.ring.drop()
            self.ring = ring
            if ring:
                ring.pick_up(self)
        else:
            print(f"{self.name} cannot hold the ring, they are defeated.")

    def __str__(self):
        return f"{self.name} the {self.race} (HP: {self.hp}, World: {self.world}, Ring: {self.ring})"
