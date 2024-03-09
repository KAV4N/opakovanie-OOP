class SpellHolder:
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)
        print(f"{spell.name} has been added to the spell holder.")

    def remove_spell(self, spell):
        if spell in self.spells:
            self.spells.remove(spell)
            print(f"{spell.name} has been removed from the spell holder.")
        else:
            print(f"{spell.name} is not in the spell holder.")

    def display_spells(self):
        print("\nSpell Holder:")
        for spell in self.spells:
            print(spell)
