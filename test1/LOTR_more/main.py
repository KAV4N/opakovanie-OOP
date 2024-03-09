from Enemy import Enemy
from Character import Character
from Hobbit import Hobbit
from World import World
from Wizard import Wizard
from SpellHolder import SpellHolder
from Spell import Spell
from Ring import Ring


if __name__ == "__main__":
    # Creating a World instance
    world = World()

    # Creating characters
    frodo = Hobbit("Frodo Baggins")
    gandalf = Wizard("Gandalf")
    orc = Enemy("Orc Grunt", "Orc")


    gandalf.add_spell_to_holder(Spell("Fireball", damage=40, mana_cost=30))
    gandalf.add_spell_to_holder(Spell("Ice Blast", damage=35, mana_cost=25))

    # Adding objects to the World
    world.add_object(frodo)
    world.add_object(gandalf)
    world.add_object(orc)

    world.display_world_info()

    # Frodo picks up the One Ring
    frodo.hold_ring(Ring("One Ring"))

    # Frodo sneaks
    frodo.sneak()

    # Characters take damage
    gandalf.take_damage(15)
    orc.take_damage(30)

    # Displaying World Information again
    world.display_world_info()

    # Frodo drops the One Ring
    frodo.hold_ring(None)

    # Displaying World Information after dropping the ring
    world.display_world_info()

    # Displaying the Wizard's spell holder
    gandalf.get_spell_holder().display_spells()

    # Casting spells using the Wizard's spell holder
    gandalf.cast_spell(orc, "Fireball")
    gandalf.cast_spell(orc, "Ice Blast")

    # Displaying World Information after casting spells
    world.display_world_info()