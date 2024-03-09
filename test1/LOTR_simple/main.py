
class Ring:
    def __init__(self, entity):
        self.holder = entity

    def heal(self):
        self.holder.setHp(1000000000000000000000)

class Character:
    pocet = 0

    def __init__(self, name="asda", race="adad",hp=0,ring=False):
        self._name = name
        self._race = race
        self._hp = hp
        self._ring = Ring(self)
        self._ring.heal()
        Character.pocet += 1

    def getName(self):
        return self._name

    def getRace(self):
        return self._race

    def getHp(self):
        return self._hp

    def setHp(self,hp):
        self._hp = hp

    def setName(self, name):
        self._name = name

    def __str__(self):
        return f"Volam sa {self._name} a mam {self._hp} hp"


    def vypisAhoj():
        print("ahoj")

class Gandalf(Character):
    def __init__(self, name, mana):
        super().__init__(name=name,race="Wizard",hp=69,ring=False)

        self.isHoldingStaff = False
        self.mana = mana

    def castSpell(self):
        if self.mana-10 >= 0:
            print("zabijem bal")
            self.mana-=10
        else:
            print("oh no, L")

    def killHim(self,who):
        print(who.mana)

    def __del__(self):
        print("umieram")


class World:
    def __init__(self):
        self.worldList = []

    def addEntity(self,entity):
        self.worldList.append(entity)

    def delEntity(self, idx):
        del self.worldList[idx]

    def delEntity(self, entity):
        self.worldList.remove(entity)


world = World()
world.addEntity(Gandalf("Gandalf", 10))
world.addEntity(Gandalf("Gandalf", 1000))
world.addEntity(Character())

print(world.worldList[0].getHp())
