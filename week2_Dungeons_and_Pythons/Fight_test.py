import unittest
from Fight import Fight
from Orc import Orc
from Weapon import Weapon
from Hero import Hero


class TestFight(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Gosho", 30, "Goshko")
        self.orc = Orc("Pesho", 100, 1.3)
        self.fight = Fight(self.hero, self.orc)
        self.weapon = Weapon("qax", 40, 0.3)
        self.hero.weapon = self.weapon
        self.orc.weapon = self.weapon

    def test_simulate_fight(self):
        self.fight.simulate_fight()
        self.assertFalse(self.orc.is_alive() and self.hero.is_alive())

    def test_simulate_fight_orc_no_weapon(self):
        self.fight.simulate_fight()
        self.orc.weapon = None
        self.assertFalse(self.orc.is_alive() and self.hero.is_alive())



if __name__ == '__main__':
    unittest.main()