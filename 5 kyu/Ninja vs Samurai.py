import unittest

Position = {'high': 'h', 'low': 'l'}  # don't change this!

class Warrior:
    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        damage = 0
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        if enemy.block != position: damage += 10 if position == Position['high'] else 5
        # and even more damage if the enemy is not blocking at all
        if enemy.block == "": damage += 5
        enemy.set_health(enemy.health - damage)


    def set_health(self, new_health):
        # health cannot have negative values
        self.health = max(0, new_health)
        # if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased = True


class Tests(unittest.TestCase):
    def test_1(self):
        ninja = Warrior('Hanzo Hattori')
        samurai = Warrior('Ryoma Sakamoto')
        samurai.block = 'l'
        ninja.attack(samurai, 'h')
        self.assertEqual(samurai.health, 90,
                           'Expected samurai health to equal 90, instead got ' + str(samurai.health))


if __name__ == "__main__":
    unittest.main()