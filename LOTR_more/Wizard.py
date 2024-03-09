from Character import  Character
from SpellHolder import SpellHolder

class Wizard(Character):
    def __init__(self, name, mana=100):
        super().__init__(name, race="Wizard", hp=120)
        self.mana = mana
        self.spell_holder = SpellHolder()

    def cast_spell(self, target, spell_name):
        spell = self.get_spell(spell_name)
        if spell:
            if self.mana >= spell.mana_cost:
                self.mana -= spell.mana_cost
                damage = spell.damage
                target.take_damage(damage)
                print(f"{self.name} casts {spell.name} on {target.name}! Damage: {damage}, Mana: {self.mana}")
            else:
                print(f"{self.name} doesn't have enough mana to cast {spell.name}.")
        else:
            print(f"{self.name} does not know the spell {spell_name}.")

    def restore_mana(self, amount):
        self.mana = min(100, self.mana + amount)
        print(f"{self.name} restores {amount} mana. Current Mana: {self.mana}")

    def check_mana_status(self):
        print(f"{self.name}'s current mana: {self.mana}")

    def use_staff(self):
        print(f"{self.name} uses his staff for magical purposes.")

    def add_spell_to_holder(self, spell):
        self.spell_holder.add_spell(spell)

    def remove_spell_from_holder(self, spell):
        self.spell_holder.remove_spell(spell)

    def get_spell_holder(self):
        return self.spell_holder

    def get_spell(self, spell_name):
        for spell in self.spell_holder.spells:
            if spell.name.lower() == spell_name.lower():
                return spell
        return None

    def __str__(self):
        return super().__str__() + f" (Mana: {self.mana}, Spell Holder: {self.spell_holder})"
